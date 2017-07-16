from rest_framework import permissions
from .models import Librarian, Borrower


def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    if group_name.objects.filter(user=user):
        return True
    return False


class HasGroupPermission(permissions.BasePermission):
    """
    Ensure user is in required groups.
    """

    def has_permission(self, request, view):
        # Get a mapping of methods -> required group.
        if request.user.is_superuser:
            return True
        required_groups_mapping = getattr(view, 'required_groups', {})

        # Determine the required groups for this particular request method.
        required_groups = required_groups_mapping.get(request.method, [])

        # Return True if the user has all the required groups.
        for group_name in required_groups:
            if is_in_group(request.user, group_name):
                return True
        return False
