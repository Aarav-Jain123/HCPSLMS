from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='Index'),
    path('add-issue/', add_new_issue, name='Add issue')
]
