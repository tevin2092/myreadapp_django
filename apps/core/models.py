from django.db import models

class CreatedModifiedAbstract(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, null=True)
    modfied_at = models.DateTimeField(
        auto_now_add=True, null=True
    )
    


class Meta:
    abstract=True