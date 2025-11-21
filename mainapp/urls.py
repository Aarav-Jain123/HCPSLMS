from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='Index'),
    path('add-issue/', add_issue, name='Add issue'),
    path('add-book/', add_book, name='Add book'),
    path('add-publication/', add_publication, name='Add publication'),
    path('add-author/', add_author, name='Add author'),
    path('view-book/', view_book, name='View book'),
    path('view-author/', view_author, name='View Author'),
    path('view-publication/', view_publication, name='View Publication'),
]
