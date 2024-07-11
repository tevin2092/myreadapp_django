from datetime import timedelta
from django.db import models
from django.contrib.auth.models import  AbstractUser, User
# Create your models here.

class NIC(models.Model):
    nic_number = models.CharField(max_length=10, primary_key=True)
    delivery_date = models.DateField()
    # auto-calculated field from other fields
    # expiration_date = models.DateField()
    
    expiration_date = models.GeneratedField(
        expression = models.F('delivery_date') + timedelta(days=1827),
        output_field = models.DateField(),
        db_persist = True
    )

    def __str__(self) -> str:
        return f'{self.nic_number}(del: {self.delivery_date}, exp: {self.expiration_date})'
    
    class Meta:
        db_table_comment = 'National Identity Card'
        verbose_name_plural = 'NIC'


# Reader -> AbstractUser -> AbstractBaseUser -> models.Model
class Reader(AbstractUser):
    READER_TITLE = {
        # key= will be stored in the database
        # value = will be displayed to the user
        "Mr": "Mr",
        "Mrs": "Mrs",
        "Ms": "Ms",
        "Dr": "Dr"
    }
    # If no explicit primary is defined, Django will generate an id for us.
    # Class attributes will represent fields in our table.
    # By default, django fields are 'not null'
    username = models.CharField(max_length=50, primary_key=True)
    # null=True set the null field when used on the terminal
    # blank=True set the null field when used on the dashboard
    title = models.CharField(max_length=5, null=True, blank=True, choices=READER_TITLE)
    # If you want to remove the default, just set it to None
    # email = None
    # reader_set
    nic = models.OneToOneField(
        'reader.NIC', 
        related_name='reader', 
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    class Meta:
        # Define some meta data, including constraints
        db_table = 'reader'
        constraints = [
            models.CheckConstraint(
                # reader_Reader_title_check
                name='%(app_label)s_%(class)s_title_check',
                check=models.Q(title__in=['Mr', 'Mrs', 'Ms', 'Dr'])
            )
        ]