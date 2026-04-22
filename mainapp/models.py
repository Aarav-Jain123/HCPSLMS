from django.db import models
from datetime import date, timedelta
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import pandas as pd


# class Students(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#     admission_no = models.IntegerField()
    
#     student_name = models.CharField(max_length=64)
#     student_mother_name = models.CharField(max_length=64)
#     student_father_name = models.CharField(max_length=64)
    
#     student_image = models.ImageField()
#     student_father_image = models.ImageField()
#     student_mother_image = models.ImageField()
    
#     student_address = models.TextField(blank=True, null=True)
    
    # student_grade = models.IntegerField()
    # student_section = models.CharField(max_length=1)
    
#     student_phone_number_father = models.IntegerField()
#     student_phone_number_mother = models.IntegerField()
#     student_mode_of_transfer = models.CharField(max_length=8)
    
#     def __str__(self):
#         student = ", ".join(a.student_name for a in self.student_name.all())
#         class_of_student = ", ".join(p.publication_name for p in self.student_grade.all())
#         section_of_student = "".join(s.student_section for s in self.student_section.all())
#         return f"{student} of {class_of_student}{section_of_student}"    
    
class Author(models.Model):
    author_name = models.CharField(max_length=256)

    class Meta:
        ordering = ["author_name"]

    def __str__(self):
        return self.author_name


class Publication(models.Model):
    publication_name = models.CharField(max_length=256, unique=True)

    class Meta:
        ordering = ["publication_name"]

    def __str__(self):
        return self.publication_name






class Books(models.Model):
    book_code = models.CharField(max_length=256, unique=True)
    book_name = models.CharField(max_length=256)
    book_author = models.CharField(max_length=256, default='N/A')
    book_publication = models.CharField(max_length=256, default='N/A')
    book_pages = models.CharField(max_length=256, default='N/A')
    book_cost = models.CharField(max_length=256, default='N/A')
    book_language = models.CharField(max_length=256, default='N/A')
    book_edition_description = models.CharField(max_length=256, default='N/A')
    book_isbn_no = models.CharField(max_length=256, default='N/A')
    book_purchase_date = models.CharField(max_length=256, default='N/A')
    book_purchase_ref_name = models.CharField(max_length=256, default='N/A')
    book_bill_number = models.CharField(max_length=256, default='N/A')
    book_place_of_publication = models.CharField(max_length=256, default='N/A')


    class Meta:
        ordering = ["book_name"]

    def __str__(self):
        authors = ", " + self.book_author
        publication = ", " + self.book_publication
        return f"{self.book_code} - {self.book_name} by {authors} under {publication}"
        


class IssueBook(models.Model):
    book = models.ForeignKey(Books, on_delete=models.PROTECT, unique=True)
    # issue_holder = models.ManyToManyField("Students", related_name='issuebook')
    admission_no = models.IntegerField(default=0)
    
    
    student_name = models.CharField(max_length=64, default='')
    student_grade = models.IntegerField(default=0)
    student_section = models.CharField(max_length=1, default='')
    returned = models.BooleanField(default=False)
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)


    class Meta:
        ordering = ["-issue_date"]

    def save(self, *args, **kwargs):
        if not self.issue_date:
            self.issue_date = date.today()
        if not self.return_date:
            self.return_date = date.today() + timedelta(days=7)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Issue of {self.book.book_name} to {self.student_name} of class {self.student_grade}{self.student_section}."


class OverDueBook(models.Model):
    issue = models.OneToOneField("IssueBook", on_delete=models.CASCADE)
    # overdue_issue_holder = models.ManyToManyField(Students, related_name='overdueissueholder')
    student_name = models.CharField(max_length=64, default='')
    student_grade = models.IntegerField(default=0)
    admission_no = models.IntegerField(default=0)
    date_issued = models.DateField(null=True)
    date_supposed_to_be_returned = models.DateField(null=True)
    
    student_section = models.CharField(max_length=1, default='')
    
    class Meta:
        ordering = ['-issue']
        
        
            

    def __str__(self):
        return f"Issue of {self.issue.book.book_name} to {self.student_name} of {self.student_grade}{self.student_section} is overdue."









class Magazines(models.Model):
    magazine_code = models.CharField(max_length=256, unique=True)
    magazine_name = models.CharField(max_length=256)
    magazine_author = models.CharField(max_length=256, default='N/A')
    magazine_publication = models.CharField(max_length=256, default='N/A')
    magazine_pages = models.CharField(max_length=256, default='0')
    magazine_cost = models.CharField(max_length=256, default='0')
    magazine_language = models.CharField(max_length=256, default='N/A')
    magazine_edition_description = models.CharField(max_length=256, default='N/A')
    magazine_isbn_no = models.CharField(max_length=256, default='N/A')
    magazine_purchase_date = models.CharField(max_length=256, default='N/A')
    magazine_purchase_ref_name = models.CharField(max_length=256, default='N/A')
    magazine_bill_number = models.CharField(max_length=256, default='N/A')
    magazine_place_of_publication = models.CharField(max_length=256, default='N/A')

    class Meta:
        ordering = ["magazine_name"]

    def __str__(self):
        authors = ", " + self.magazine_author
        publication = ", " + self.magazine_publication
        return f"{self.magazine_code} - {self.magazine_name} by {authors} under {publication}"


class IssueMagazine(models.Model):
    magazine = models.ForeignKey(Magazines, on_delete=models.PROTECT, unique=True)
    admission_no = models.IntegerField(default=0)
    
    
    student_name = models.CharField(max_length=64, default='')
    student_grade = models.IntegerField(default=0)
    student_section = models.CharField(max_length=1, default='')
    returned = models.BooleanField(default=False)
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)


    class Meta:
        ordering = ["-issue_date"]

    def save(self, *args, **kwargs):
        if not self.issue_date:
            self.issue_date = date.today()
        if not self.return_date:
            self.return_date = date.today() + timedelta(days=7)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Issue of {self.magazine.magazine_name} to {self.student_name} of class {self.student_grade}{self.student_section}."


class OverDueMagazine(models.Model):
    issue = models.OneToOneField("IssueMagazine", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=64, default='')
    student_grade = models.IntegerField(default=0)
    admission_no = models.IntegerField(default=0)
    date_issued = models.DateField(null=True)
    date_supposed_to_be_returned = models.DateField(null=True)
    
    student_section = models.CharField(max_length=1, default='')
    
    class Meta:
        ordering = ['-issue']
        
        
    def __str__(self):
        return f"Issue of {self.issue.magazine.magazine_name} to {self.student_name} of {self.student_grade}{self.student_section} is overdue."
    




class Specimens(models.Model):
    specimen_code = models.CharField(max_length=256, unique=True)
    specimen_name = models.CharField(max_length=256)

    class Meta:
        ordering = ["specimen_name"]

    def __str__(self):
        return f"{self.specimen_code} - {self.specimen_name}"








class ExcelFileUpload(models.Model):
    file = models.FileField(
            upload_to='uploads/',
            validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'csv'])]
    )
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        df=pd.read_excel(f'{self.file.name}')
        df.columns=["Item_Type",	"Category_Name",	"Book_Title",	"ISBN_No",	"Author_Name",	"Publisher_Name",	"Edition_Description",	"No_of_Pages",	"Language",	"Issue_of_Date",	"Book_Cost",	"Issue_Flag",	"Purchase_Date",	"Purchase_Ref_Name",	"Accession_No",	"Book_Series_Type",	"Bill_Number",	"Place_of_Publication"]
        for index, row in df.iterrows():
            if row["Item_Type"] == "MAGAZINES":
                try:
                    magazines = Magazines.objects.get(magazine_code=row["Accession_No"])
                except Magazines.DoesNotExist:
                    magazines = Magazines(
magazine_code = row["Accession_No"],
magazine_name = row["Book_Title"],
magazine_author = row["Author_Name"],
magazine_publication = row["Publisher_Name"],
magazine_pages = row["No_of_Pages"],
magazine_cost = row["Book_Cost"],
magazine_language = row["Language"],
magazine_edition_description = row["Edition_Description"],
magazine_isbn_no = row['ISBN_No'],
magazine_purchase_date = row['Purchase_Date'],
magazine_purchase_ref_name = row['Purchase_Ref_Name'],
magazine_bill_number = row['Bill_Number'],
magazine_place_of_publication = row["Place_of_Publication"],
)
                    magazines.save()
        
            else:
                try:
                    books = Books.objects.get(book_code=row["Accession_No"])
                except Books.DoesNotExist:
                    books = Books(
book_code = row["Accession_No"],
book_name = row["Book_Title"],
book_author = row["Author_Name"],
book_publication = row["Publisher_Name"],
book_pages = row["No_of_Pages"],
book_cost = row["Book_Cost"],
book_language = row["Language"],
book_edition_description = row["Edition_Description"],
book_isbn_no = row['ISBN_No'],
book_purchase_date = row['Purchase_Date'],
book_purchase_ref_name = row['Purchase_Ref_Name'],
book_bill_number = row['Bill_Number'],
book_place_of_publication = row["Place_of_Publication"],
)
                    books.save()
