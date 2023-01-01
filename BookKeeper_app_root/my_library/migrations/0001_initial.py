# Generated by Django 4.1.3 on 2022-12-26 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ["last_name", "first_name"],
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("book_cover", models.ImageField(upload_to="media/photos/covers/")),
                ("title", models.CharField(max_length=50)),
                ("language", models.CharField(max_length=200)),
                (
                    "summary",
                    models.TextField(
                        help_text="Enter a brief description of the book",
                        max_length=1000,
                    ),
                ),
                ("pg_num", models.IntegerField()),
                ("status", models.CharField(max_length=200)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="my_library.author",
                        verbose_name="books",
                    ),
                ),
            ],
        ),
    ]