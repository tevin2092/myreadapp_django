# Generated by Django 5.0.6 on 2024-07-11 07:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0005_alter_book_options_alter_bookauthor_options_and_more"),
        ("myread", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="statuspercent",
            options={"verbose_name_plural": "Status Percentages"},
        ),
        migrations.AlterUniqueTogether(
            name="myread",
            unique_together={("book_isbn", "reader_username", "start_read_date")},
        ),
    ]
