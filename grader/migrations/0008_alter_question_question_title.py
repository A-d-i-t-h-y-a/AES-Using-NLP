# Generated by Django 5.1.1 on 2024-10-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0007_auto_20180812_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.TextField(),
        ),
    ]