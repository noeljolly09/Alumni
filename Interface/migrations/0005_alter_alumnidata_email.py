# Generated by Django 3.2.7 on 2021-11-24 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Interface', '0004_auto_20211105_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnidata',
            name='Email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
