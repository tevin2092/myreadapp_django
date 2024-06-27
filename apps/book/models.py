from django.db import models
from django.contrib.postgres.fields import ArrayField # postgresql specific

# Create your models here.

class Book(models.Model):
    BOOK_CATEGORY = {
        "pr": "programming",
        "ar": "art",
        "hi": "history",
        "po": "politics",
        "ot": "others"
    }
    BOOK_FORMAT = {
        "eb": "ebook",
        "hc": "hardcover"
    }
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    page_count = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=2, choices=BOOK_CATEGORY, default='pr')
    published_date = models.IntegerField()
    publisher = models.CharField(max_length=50)
    authors = ArrayField(ArrayField(models.CharField(max_length=50)))
    lang = models.CharField(max_length=50)
    edition = models.SmallIntegerField(null=True, blank=True)
    book_format_ = models.CharField(max_length=2, choices=BOOK_FORMAT)