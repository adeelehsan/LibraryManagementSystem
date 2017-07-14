from rest_framework import viewsets
from rest_framework import generics
from django.db.models import Count
from .models import Books, Borrower, Librarian, BookIssueRecord
from .serializers import BookSerializer, BorrowerSerializer,\
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
    serializer_class = BorrowerSerializer
    queryset = Borrower.objects.all()


class LibrarianViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing librarian instances.
    """
    serializer_class = LibrarianSerializer
    queryset = Librarian.objects.all()


class BookIssueRecordViewSet(viewsets.ModelViewSet):
    """
        A viewset for viewing and editing Library book issuance record instances.
    """
    serializer_class = BookIssueRecordSerializer
    queryset = BookIssueRecord.objects.all()

    def perform_create(self, serializer):
        if self.is_available:
            borrower = Borrower.objects.get(pk=1)
            book = Books.objects.get(pk=1)
            issuer = Librarian.objects.get(pk=1)
            serializer.save(borrower=borrower, book=book, issuer=issuer)

    def is_available(self):
        """
        that function availabilty to rent out on the basis on Total
        copies available and No of copies already rented
        """
        book = self.request.data['borrower']
        copies_rented = BookIssueRecord.objects.filter(book_id=book.id, return_date__isnull=True).Count('book')
        if copies_rented < book.copies_availabe:
            return True
        return False

