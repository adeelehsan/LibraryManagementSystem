from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    no_of_copies_available = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Borrower_User(AbstractUser):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Librarian_User(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BookIssueRecord(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    issuer = Librarian_User.pk
    issue_date = models.DateField(null=False)
    due_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    fine_amount = models.IntegerField(null=True)