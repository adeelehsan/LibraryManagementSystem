from rest_framework import viewsets
from rest_framework import generics
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


class BookIssueRecordView(generics.ListCreateAPIView):
    """
        A viewset for viewing and editing Library book issuance record instances.
    """
    serializer_class = BookIssueRecordSerializer

    def perform_create(self, serializer):
        if self.is_available:
            borrower = Borrower.objects.get(pk=1)
            book = Books.objects.get(pk=1)
            serializer.save(issuer=self.request.user, borrower=borrower, book=book)

    def is_available(self):
        return True
