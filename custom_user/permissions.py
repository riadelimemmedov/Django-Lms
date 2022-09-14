from rest_framework import permissions
from .models import CustomUser


#!AdminRequired
class AdminRequired(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == CustomUser.ADMIN_ROLE_CODE
    
#!BorrowerRequired
class BorrowerRequired(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == CustomUser.BORROWER_ROLE_CODE

#!LibrarianRequired
class LibrarianRequired(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == CustomUser.LIBRARIAN_ROLE_CODE