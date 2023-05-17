# Generated by Django 3.2 on 2023-05-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='レビュー内容'),
        ),
    ]