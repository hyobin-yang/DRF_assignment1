# Generated by Django 4.2.3 on 2023-07-09 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0021_comment_nickname"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="nickname", new_name="user",
        ),
    ]