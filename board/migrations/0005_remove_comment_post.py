# Generated by Django 4.2.3 on 2023-07-06 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0004_comment"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="post",),
    ]