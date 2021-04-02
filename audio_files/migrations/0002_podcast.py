# Generated by Django 3.1.1 on 2021-04-02 07:21

import audio_files.customfield
import audio_files.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploadedtime', models.DateTimeField(validators=[audio_files.models.validate_datetime])),
                ('host', models.CharField(max_length=100)),
                ('participants', audio_files.customfield.CommaSeparatedValuesField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]