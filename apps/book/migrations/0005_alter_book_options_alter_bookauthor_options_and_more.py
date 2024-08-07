# Generated by Django 5.0.6 on 2024-07-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0004_tag_book_tags"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={
                "default_related_name": "%(app_label)s_%(model_name)s",
                "ordering": ("-title",),
            },
        ),
        migrations.AlterModelOptions(
            name="bookauthor",
            options={"verbose_name_plural": "Books and Authors"},
        ),
        migrations.AddField(
            model_name="book",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="modified_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(through="book.BookAuthor", to="book.author"),
        ),
        migrations.AlterField(
            model_name="book",
            name="book_format",
            field=models.CharField(
                choices=[("eb", "ebook"), ("hc", "hardcover")],
                default="eb",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="tags",
            field=models.ManyToManyField(to="book.tag"),
        ),
        migrations.AlterField(
            model_name="bookauthor",
            name="role",
            field=models.CharField(
                choices=[
                    ("author", "Author"),
                    ("co_author", "Co-Author"),
                    ("editor", "Editor"),
                ],
                default="author",
                max_length=10,
            ),
        ),
    ]
