from django.db import models

# Create your models here.
class CreatedModifiedAbstract(models.Model):
    # This should default to the current date and time 
    created_at = models.DateTimeField(
        auto_now_add=True, null=True)
    # This should be change each time a row is modified
    modified_at = models.DateTimeField(
        auto_now=True, null=True)

    class Meta:
        abstract = True