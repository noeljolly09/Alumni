# Generated by Django 2.1.7 on 2021-11-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsdata',
            name='event_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='event_images/'),
        ),
    ]
