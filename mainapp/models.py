from django.db import models
from datetime import date, timedelta
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


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
    author_link = models.CharField(max_length=1024, unique=True)

    class Meta:
        ordering = ["author_name"]

    def __str__(self):
        return self.author_name


class Publication(models.Model):
    publication_name = models.CharField(max_length=256, unique=True)
    publication_link = models.CharField(max_length=1024)

    class Meta:
        ordering = ["publication_name"]

    def __str__(self):
        return self.publication_name






class Books(models.Model):
    book_code = models.CharField(max_length=256, unique=True)
    book_name = models.CharField(max_length=256)
    book_author = models.ManyToManyField("Author", related_name='books')
    book_link = models.CharField(max_length=1024)
    book_publication = models.ManyToManyField("Publication", related_name='books')

    class Meta:
        ordering = ["book_name"]

    def __str__(self):
        authors = ", ".join(a.author_name for a in self.book_author.all())
        pubs = ", ".join(p.publication_name for p in self.book_publication.all())
        return f"{self.book_code} - {self.book_name} by {authors} under {pubs}"


class IssueBook(models.Model):
    book = models.ForeignKey(Books, on_delete=models.PROTECT)
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
    magazine_author = models.ManyToManyField("Author", related_name='magazines')
    magazine_link = models.CharField(max_length=1024)
    magazine_publication = models.ManyToManyField("Publication", related_name='magazines')

    class Meta:
        ordering = ["magazine_name"]

    def __str__(self):
        authors = ", ".join(a.author_name for a in self.magazine_author.all())
        pubs = ", ".join(p.publication_name for p in self.magazine_publication.all())
        return f"{self.magazine_code} - {self.magazine_name} by {authors} under {pubs}"


class IssueMagazine(models.Model):
    magazine = models.ForeignKey(Magazines, on_delete=models.PROTECT)
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
