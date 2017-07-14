from rest_framework import serializers
from LibraryManagement.models import Books, Borrower,\
    Librarian, BookIssueRecord


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('id', 'name',
                  'isbn', 'author', 'copies_available')


class BookIssueRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookIssueRecord
        fields = ('id', 'borrower', 'book', 'issuer',
                  'issue_date', 'due_date', 'return_date', 'fine_amount')


class BorrowerSerializer(serializers.ModelSerializer):
    record = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                 view_name='bookissuerecord-detail',
                                                 required=False)

    class Meta:
        model = Borrower
        fields = ('id', 'name', 'address', 'record')


class LibrarianSerializer(serializers.ModelSerializer):
    record = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                 view_name='bookissuerecord-detail',
                                                 required=False)

    class Meta:
        model = Librarian
        fields = ('id', 'name', 'address', 'record')
