from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from datetime import date

from .permissions import HasGroupPermission
from .models import Books, Borrower, Librarian, BookIssueRecord
from .serializers import BookSerializer, BorrowerSerializer, \
    LibrarianSerializer, BookIssueRecordSerializer


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    serializer_class = BookSerializer
    queryset = Books.objects.all()


class BorrowerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Borrower user instances.
    """
    permission_classes = (HasGroupPermission, )
    required_groups = {
        'GET': [Borrower, Librarian],
        'POST': [Librarian],
        'PUT': [Borrower],
        'DELETE': [Librarian]
    }
    serializer_class = BorrowerSerializer

    def get_queryset(self):
        """
        This view should return a list of all the borrower
        for the currently authenticated user.
        """
        user = self.request.user
        if Borrower.objects.filter(user=user):
            borrower = Borrower.objects.filter(user=user)
            return borrower
        else:
            borrower_list = Borrower.objects.all()
            return borrower_list


class LibrarianViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing librarian instances.
    """
    permission_classes = (HasGroupPermission, )
    required_groups = {
        'GET': [Librarian],
        'PUT': [Librarian],
    }
    serializer_class = LibrarianSerializer

    def get_queryset(self):
        """
        This view should return a list of all the borrower
        for the currently authenticated user.
        """
        user = self.request.user
        if Librarian.objects.filter(user=user):
            librarian = Librarian.objects.filter(user=user)
            return librarian
        else:
            librarian_list = Librarian.objects.all()
            return librarian_list


class BookIssueRecordViewSet(viewsets.ModelViewSet):
    """
        A view set for viewing and editing Library book issuance record instances.
    """
    permission_classes = (HasGroupPermission,)
    required_groups = {
        'GET': [Librarian, Borrower],
        'POST': [Librarian],
        'PUT': [Librarian],
        'DELETE': [Librarian]
    }
    serializer_class = BookIssueRecordSerializer
    queryset = BookIssueRecord.objects.all()

    def perform_create(self, serializer):
        if self.is_available() and self.already_rented() and self.subscription_validity():
            book_id = self.request.data['book']
            borrower_id = self.request.data['borrower']
            issuer_id = self.request.data['issuer']
            borrower = Borrower.objects.get(pk=borrower_id)
            book = Books.objects.get(pk=book_id)
            issuer = Librarian.objects.get(pk=issuer_id)
            serializer.save(borrower=borrower, book=book, issuer=issuer)
        else:
            return Response({'Fail': 'Sorry You can not borrow requested book'},
                            status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
            Update the record whenever book is returned.
        """
        queryset = BookIssueRecord.objects.all()
        issue_record = get_object_or_404(queryset, pk=pk)
        issue_record.return_date = date.today()
        issue_record.save()
        return Response(status=status.HTTP_206_PARTIAL_CONTENT)

    def is_available(self):
        """
            that function availability to rent out on the basis on Total
            copies available and No of copies already rented
        """
        book_id = self.request.data['book']
        queryset = Books.objects.all()
        book = get_object_or_404(queryset, pk=book_id)
        copies_rented = BookIssueRecord.objects.filter(book_id=book.id, return_date__isnull=True).count()
        if copies_rented < book.copies_available:
            return True
        return False

    def already_rented(self):
        """
            check if user has already rented requested book or not
        """
        borrower_id = self.request.data['borrower']
        book_id = self.request.data['book']
        rented = Borrower.objects.filter(pk=borrower_id, record__book__id=book_id,
                                         record__return_date__isnull=True)
        if not rented:
            return True
        return False

    def subscription_validity(self):
        """
            check if user subscription has ended or not
        """
        borrower_id = self.request.data['borrower']
        queryset = Borrower.objects.all()
        borrower = get_object_or_404(queryset, pk=borrower_id)
        if borrower.subscription_end_date >= date.today():
            return True
        return False