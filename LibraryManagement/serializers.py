from rest_framework import serializers
from LibraryManagement.models import Books, Borrower,\
    Librarian, BookIssueRecord


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('id', 'name',
                  'isbn', 'author', 'no_of_copies_available')


class BorrowerSerializer(serializers.ModelSerializer):
    record = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                 view_name='bookissuerecord-detail',
                                                 required=False)

    class Meta:
        model = Borrower
        fields = ('id', 'username', 'password', 'address', 'record')


class LibrarianSerializer(serializers.ModelSerializer):
    record = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                 view_name='bookissuerecord-detail',
                                                 required=False)

    class Meta:
        model = Librarian
        fields = ('id', 'username', 'password', 'address', 'record')


class BookIssueRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookIssueRecord
        fields = ('id', 'borrower', 'book', 'issuer',
                  'issue_date', 'due_date', 'return_date', 'fine_amount')
