from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ["book_code", "book_name", "book_author", "book_link", "book_publication"]
        

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["author_name", "author_link"]


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ["publication_name", "publication_link"]


class IssueForm(forms.ModelForm):
    class Meta:
        model = IssueBook
        fields = ["book", "student_name", "student_grade", "student_section", "admission_no"]