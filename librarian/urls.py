from django.urls import path
from .views import *

app_name = 'librarian'
urlpatterns = [
    path('',LibrarianCreate.as_view(),name='librarian-create'),
    path('delete-librarian/<int:pk>/',LibrarianDelete.as_view(),name='librarian-delete')
]
