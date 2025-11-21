from django.contrib import admin
from .models import *
from django.utils import timezone

# Register your models here.
admin.site.site_header = "HCPSLMS"
admin.site.site_title = "Holy Child Public School Library Management Software"
admin.site.index_title = "Welcome to Holy Child Public School Library Management Software"

admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Publication)
admin.site.register(IssueBook)
admin.site.register(OverDueBook)
admin.site.register(Students)

class IssueBookAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        self.check_overdue()
        return super().changelist_view(request, extra_context)

    def check_overdue(self):
        today = timezone.now().date()
        issued_books = IssueBook.objects.filter(return_date=today, returned=False)

        for book in issued_books:
            OverdueBook.objects.get_or_create(
                issue=book,
                defaults={
                    "issue": book.user,
                    "book": book.book,
                    "due_date": book.return_date,
                }
            )

# Fix from line 27