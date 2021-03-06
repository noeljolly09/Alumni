# Generated by Django 2.1.7 on 2021-11-24 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0005_alter_alumnidata_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnidata',
            name='Bio',
            field=models.CharField(default='Here is My Bio', max_length=100),
        ),
        migrations.AddField(
            model_name='alumnidata',
            name='Designation',
            field=models.CharField(default='Software Developer', max_length=50),
        ),
        migrations.AlterField(
            model_name='alumnidata',
            name='Profile_image',
            field=models.ImageField(blank=True, default='default.jpg', height_field='600', null=True, upload_to='profile_images/', width_field='600'),
        ),
    ]
