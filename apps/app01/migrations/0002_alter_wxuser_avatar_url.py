# Generated by Django 3.2.18 on 2023-03-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wxuser',
            name='avatar_url',
            field=models.URLField(null=True, verbose_name='头像'),
        ),
    ]
