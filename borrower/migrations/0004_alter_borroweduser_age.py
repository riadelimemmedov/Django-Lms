# Generated by Django 4.1.1 on 2022-09-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrower', '0003_alter_borroweduser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borroweduser',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
