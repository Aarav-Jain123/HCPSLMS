from django.db import models
from autoslug import AutoSlugField
from datetime import date, timedelta
from django.core.validators import MaxValueValidator


class Author(models.Model):
    author_name = models.CharField(max_length=256)
    author_link = models.URLField()

    class Meta:
        ordering = ["author_name"]

    def __str__(self):
        return self.author_name


class Publication(models.Model):
    publication_name = models.CharField(max_length=256)
    publication_link = models.URLField()

    class Meta:
        ordering = ["publication_name"]

    def __str__(self):
        return self.publication_name


class Books(models.Model):
    book_code = models.CharField(max_length=256, unique=True)
    book_name = models.CharField(max_length=256)
    book_author = models.ManyToManyField("Author", related_name='books')
    book_link = models.URLField()
    book_publication = models.ManyToManyField("Publication", related_name='books')

    class Meta:
        ordering = ["book_name"]

    def __str__(self):
        authors = ", ".join(a.author_name for a in self.book_author.all())
        pubs = ", ".join(p.publication_name for p in self.book_publication.all())
        return f"{self.book_code} - {self.book_name} by {authors} under {pubs}"


class IssueBook(models.Model):
    book = models.ForeignKey(Books, on_delete=models.PROTECT)
    admission_no = models.IntegerField(validators=[MaxValueValidator(999999)])
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    issue_id = AutoSlugField(populate_from='book', unique=True)

    class Meta:
        ordering = ["-issue_date"]

    def save(self, *args, **kwargs):
        if not self.return_date:
            self.return_date = date.today() + timedelta(days=7)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Issue of {self.book.book_name} to {self.admission_no}."


class OverDueBook(models.Model):
    issue = models.OneToOneField("IssueBook", on_delete=models.CASCADE)
    over_due_id = AutoSlugField(populate_from='issue__issue_id', unique=True)

    def __str__(self):
        return f"Issue of {self.issue.book.book_name} to {self.issue.admission_no} is overdue."
