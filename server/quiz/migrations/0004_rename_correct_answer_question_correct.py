# Generated by Django 4.1.4 on 2022-12-07 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_question_correct_answer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='correct_answer',
            new_name='correct',
        ),
    ]
