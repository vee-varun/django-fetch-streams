# Generated by Django 2.1.5 on 2021-10-08 11:26

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DnaStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('stream_id', models.CharField(db_index=True, max_length=100)),
                ('created_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated_on', models.DateTimeField(blank=True, db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StreamData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.CharField(max_length=100, unique=True)),
                ('raw_data_dict', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, help_text='contains data received from stream', null=True)),
                ('status', models.IntegerField(choices=[(1, 'PENDING'), (2, 'FETCHED')], db_index=True, default=1)),
                ('action', models.CharField(choices=[('add', 'ADD'), ('rep', 'UPDATE'), ('del', 'DELETE')], db_index=True, default='add', max_length=5)),
                ('created_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('stream_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fetch_stream.DnaStream')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='streamdata',
            unique_together={('data_id', 'action')},
        ),
    ]
