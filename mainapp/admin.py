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
# admin.site.register(IssueBook) this will follow default architecture
admin.site.register(OverDueBook)
# admin.site.register(Students)


@admin.register(IssueBook) # this will make it more dynamic and help load the following class
class IssueBookAdmin(admin.ModelAdmin):

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
                    "issue_date": issues.issue_date,
                    "return_date": issues.return_date,
                    "issue_id": issues.issue_id
                }
            )
