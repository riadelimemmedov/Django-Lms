from django.urls import path
from .views import *

app_name = 'library'
urlpatterns = [
    path('',LibraryListCreate.as_view(),name='library-list-create'),
    path('<int:pk>/',LibraryDetail.as_view(),name='library-detail'),
    path('register/librarian/account/',RegisterLibrarian.as_view(),name='librarian-register-account'),
    path('create/librarian/',LibrarianListCreate.as_view(),name='librarian-create'),
    path('delete/librarian/account/<int:pk>/',LibrarianDelete.as_view(),name='librarian-delete-account')
]
