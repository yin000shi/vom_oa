# Generated by Django 2.1 on 2019-10-08 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nporder', '0005_auto_20191007_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nporder',
            name='creator',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
