# Generated by Django 2.1 on 2020-01-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nporder', '0002_auto_20200122_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nporder',
            name='direction',
            field=models.CharField(choices=[('基础版', '基础版'), ('增强版', '增强版'), ('完整版', '完整版')], default='添加', max_length=20),
        ),
    ]
