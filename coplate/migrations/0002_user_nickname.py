# Generated by Django 4.0.1 on 2022-02-11 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]