# Generated by Django 4.2.4 on 2023-09-06 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0002_lettercomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LetterComment',
        ),
    ]
