# Generated by Django 2.0.4 on 2019-03-23 09:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # NOQA
                ('document_name', models.TextField()),
                ('document', models.FileField(upload_to='documents/%Y/%m/%d/')),  # NOQA
            ],
        ),
        migrations.CreateModel(
            name='FileData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # NOQA
                ('token', models.CharField(max_length=4, unique=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),  # NOQA
                ('upload_date', models.DateTimeField(default=datetime.datetime(2019, 3, 23, 14, 30, 7, 937478))),  # NOQA
                ('delete_date', models.DateTimeField(default=datetime.datetime(2019, 3, 24, 14, 30, 7, 937601))),  # NOQA
            ],
        ),
        migrations.AddField(
            model_name='fileaddress',
            name='token',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_data', to='uploader.FileData'),  # NOQA
        ),  # NOQA
    ]
