from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Books(models.Model):
    """
        An Book class - to describe book in the system.
    """
    name = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    copies_available = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Borrower(models.Model):
    """
        An Borrower class - to describe book borrower in the system.
    """
    # user = models.OneToOneRel(User)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # subscription_end_date = models.DateField()

    def __str__(self):
        return self.name


class Librarian(models.Model):
    """
        An Librarian class - to describe librarian in the system.
    """
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BookIssueRecord(models.Model):
    """
        An BookIssueRecord class - to describe book's borrow in the system.
    """
    borrower = models.ForeignKey(Borrower, related_name='record', on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    issuer = models.ForeignKey(Librarian, related_name='record', on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now=True)
    due_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    fine_amount = models.IntegerField(null=True)