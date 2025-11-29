from django.contrib import admin
from .models import *
from django.utils import timezone

# Register your models here.
admin.site.site_header = "HCPSLMS"
admin.site.site_title = "Holy Child Public School Library Management Software"
admin.site.index_title = "Welcome to Holy Child Public School Library Management Software - By Aarav Jain of class IX A 2025-26"


admin.site.register(OverDueBook)
admin.site.register(OverDueMagazine)


@admin.register(IssueBook) # this will make it more dynamic and help load the following class
class IssueBookAdmin(admin.ModelAdmin):
    raw_id_fields = ['book']
    search_fields = ['student_name', 'student_grade', 'admission_no']
    def changelist_view(self, request, extra_context=None):
        self.check_overdue()
        return super().changelist_view(request, extra_context)

    def check_overdue(self):
        today = timezone.now().date()
        issued_books = IssueBook.objects.filter(return_date__lt=today, returned=False)

        for issues in issued_books:
            OverDueBook.objects.get_or_create(
                issue=issues,
                defaults={
                    "student_name": issues.student_name,
                    "student_grade": issues.student_grade,
                    "student_section": issues.student_section,
                    "admission_no": issues.admission_no,
                    "date_issued": issues.issue_date,
                    "date_supposed_to_be_returned": issues.return_date,
                }
            )
        

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    search_fields = [
        'book_code',
        'book_name',
        'book_author__author_name',
        'book_publication__publication_name'
]
    raw_id_fields = ['book_author', 'book_publication']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['author_name']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    search_fields = ['publication_name']


@admin.register(IssueMagazine) # this will make it more dynamic and help load the following class
class IssueMagazineAdmin(admin.ModelAdmin):
    raw_id_fields = ['magazine']
    search_fields = ['student_name', 'student_grade', 'admission_no']
    def changelist_view(self, request, extra_context=None):
        self.check_overdue()
        return super().changelist_view(request, extra_context)

    def check_overdue(self):
        today = timezone.now().date()
        issued_magazine = IssueMagazine.objects.filter(return_date__lt=today, returned=False)

        for issues in issued_magazine:
            OverDueMagazine.objects.get_or_create(
                issue=issues,
                defaults={
                    "student_name": issues.student_name,
                    "student_grade": issues.student_grade,
                    "student_section": issues.student_section,
                    "admission_no": issues.admission_no,
                    "date_issued": issues.issue_date,
                    "date_supposed_to_be_returned": issues.return_date,
                }
            )
        

@admin.register(Magazines)
class MagazinesAdmin(admin.ModelAdmin):
    search_fields = [
        'magazine_code',
        'magazine_name',
        'magazine_author__author_name',
        'magazine_publication__publication_name'
]
    raw_id_fields = ['magazine_author', 'magazine_publication']


@admin.register(Specimens)
class SpecimensAdmin(admin.ModelAdmin):
    search_fields = ['specimen_code', 'specimen_name']

