# Generated by Django 4.0.2 on 2022-03-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_first_name_customuser_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
