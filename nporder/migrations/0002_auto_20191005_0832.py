# Generated by Django 2.1 on 2019-10-05 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nporder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nporder',
            name='creator',
            field=models.ForeignKey(default='徐凯', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
