# Generated by Django 4.1.1 on 2022-09-18 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='return_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
