# Generated by Django 2.1 on 2019-11-10 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SelfDrivePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(max_length=50)),
                ('order_time', models.DateTimeField(blank=True, null=True)),
                ('phone_no', models.CharField(max_length=20)),
                ('is_installed', models.BooleanField(default=True)),
                ('city', models.CharField(max_length=20)),
                ('point', models.CharField(max_length=10)),
                ('is_handovered', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
