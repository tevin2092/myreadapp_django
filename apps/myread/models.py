from django.db import models
from django.contrib.postgres.fields import IntegerRangeField
from django.contrib.postgres.validators import (
    RangeMaxValueValidator,
    RangeMinValueValidator
)
# Create your models here.

class MyRead(models.Model):
    book_isbn = models.ForeignKey('book.Book', on_delete=models.CASCADE) # <app-name>.<class>
    reader_username = models.ForeignKey('reader.Reader', on_delete=models.CASCADE)
    # PositiveSmallIntegerField by default creates a check key with the name:
    # myread_myread_percentage_read_check
    percentage_read  = models.PositiveSmallIntegerField(null=True, blank=True)
    start_read_date = models.DateField(null=True, blank=True)
    end_read_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('book_isbn', 'reader_username', 'start_read_date')
        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_per_read_check',
                check=models.Q(
                    percentage_read__gte=0,
                    percentage_read__lte=100
                    )
            ),
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_end_read_start_read_date_check',
                check=models.Q(end_read_date__gt=models.F('start_read_date'))
            ),
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_per_read_start_read_date_check',
                check=(
                    models.Q(
                        percentage_read__exact=0,
                        start_read_date__isnull=True
                    )
                    | models.Q(
                        percentage_read__gt=0,
                        start_read_date__isnull=False
                    )
                )
            ),
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_per_read_end_read_date_check',
                check=(
                    models.Q(
                        percentage_read__exact=100,
                        end_read_date__isnull=False
                    )
                    | models.Q(
                        percentage_read__lt=100,
                        end_read_date__isnull=True
                    )
                )
            ),

        ]

    def __str__(self) -> str:
        return f'{self.reader_username}({self.book_isbn})'

class StatusPercent(models.Model):
    SP_CHOICE ={
        "pending": "Pending",
        "reading": "Reading",
        "done": "Done"
    }
    percentage_read_range = IntegerRangeField(
        null=True,
        blank=True,
        validators = [RangeMinValueValidator(0), RangeMaxValueValidator(101)]
    )
    read_status = models.CharField(max_length=10, choices=SP_CHOICE, default='pending')

    class Meta:
        verbose_name_plural = 'Status Percentages'
        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_read_status_check',
                check=models.Q(read_status__in=['pending', 'reading', 'done'])
            )
        ]

    def __str__(self) -> str:
        # But when dealing with model's method, migration is not needed.
        return f'{self.percentage_read_range}({self.read_status})'