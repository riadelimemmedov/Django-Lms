# Generated by Django 4.1.1 on 2022-09-16 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
        ('borrower', '0007_alter_borroweduser_borrowed_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borroweduser',
            name='borrowed_library',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.library'),
        ),
    ]