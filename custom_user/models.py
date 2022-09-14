from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#*CustomUser
class CustomUser(AbstractUser):
    ADMIN_ROLE_CODE = 'ADMIN'
    BORROWER_ROLE_CODE = 'BORROWER'
    LIBRARIAN_ROLE_CODE = 'LIBRARIAN'
    USER_ROLES = (
        (ADMIN_ROLE_CODE, "ADMIN"),
        (BORROWER_ROLE_CODE, "BORROWER"),
        (LIBRARIAN_ROLE_CODE, "LIBRARIAN"),
    )
    role = models.CharField(max_length=10,choices=USER_ROLES,default="BORROWER")
    
