# Generated by Django 4.0.2 on 2023-05-01 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(blank=True, default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='taskmaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiryNo', models.IntegerField()),
                ('timetaken', models.IntegerField()),
                ('comments', models.TextField(default=None)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.terms')),
            ],
        ),
    ]
