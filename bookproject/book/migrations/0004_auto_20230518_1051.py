# Generated by Django 3.2 on 2023-05-18 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20230517_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '書籍', 'verbose_name_plural': '書籍'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'レビュー状況', 'verbose_name_plural': 'レビュー状況'},
        ),
    ]
