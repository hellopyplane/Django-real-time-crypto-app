# Generated by Django 3.1.1 on 2020-09-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
