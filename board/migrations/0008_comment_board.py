# Generated by Django 4.2.3 on 2023-07-08 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0007_alter_comment_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="board",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="board.board",
            ),
        ),
    ]