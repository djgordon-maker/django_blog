# Generated by Django 3.2.7 on 2021-09-16 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="modified_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="published_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="Catagory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True)),
                (
                    "posts",
                    models.ManyToManyField(
                        blank=True, related_name="categories", to="blogging.Post"
                    ),
                ),
            ],
        ),
    ]
