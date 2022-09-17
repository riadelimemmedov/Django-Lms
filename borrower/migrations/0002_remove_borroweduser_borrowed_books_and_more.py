# Generated by Django 4.1.1 on 2022-09-17 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
        ('borrower', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borroweduser',
            name='borrowed_books',
        ),
        migrations.AddField(
            model_name='borroweduser',
            name='borrowed_books',
            field=models.ManyToManyField(blank=True, related_name='borrowed_user', to='book.book'),
        ),
    ]