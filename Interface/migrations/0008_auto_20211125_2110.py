# Generated by Django 2.1.7 on 2021-11-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0007_auto_20211124_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnidata',
            name='Phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
