# Generated by Django 4.2.3 on 2023-07-08 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0014_remove_comment_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="board.board"
            ),
        ),
    ]
