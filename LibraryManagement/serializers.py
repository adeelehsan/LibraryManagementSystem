from django.contrib.auth.models import User
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
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password')

    class Meta:
        model = Borrower
        fields = ('id', 'username', 'password', 'address', 'record')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(username=user_data['username'],
                                        password=user_data['password'])
        user.save()
        borrower = Borrower.objects.create(user=user, **validated_data)
        return borrower


class LibrarianSerializer(serializers.ModelSerializer):
    record = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                 view_name='bookissuerecord-detail',
                                                 required=False)
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password')

    class Meta:
        model = Librarian
        fields = ('id', 'username', 'password', 'address', 'record')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(username=user_data['username'],
                                        password=user_data['password'])
        user.save()
        librarian = Librarian.objects.create(user=user, **validated_data)
        return librarian
