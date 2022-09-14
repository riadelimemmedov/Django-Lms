from django.urls import path
from .views import *

app_name = 'library'
urlpatterns = [
    path('',LibraryList.as_view(),name='library-list'),
    path('<int:pk>/',LibraryDetail.as_view(),name='library-detail')
]
