# Generated by Django 4.2.5 on 2023-12-03 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_taskmaster_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmaster',
            name='userid',
            field=models.TextField(blank=True),
        ),
    ]
