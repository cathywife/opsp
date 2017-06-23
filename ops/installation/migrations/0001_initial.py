# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 04:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(db_column='cabinet_id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='cabinet_name', max_length=100, null=True)),
                ('size', models.IntegerField(blank=True, db_column='cabinet_size', null=True)),
            ],
            options={
                'db_table': 'cabinet',
            },
        ),
        migrations.CreateModel(
            name='Contacter',
            fields=[
                ('id', models.AutoField(db_column='contacter_id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('dept', models.CharField(blank=True, max_length=30, null=True)),
                ('company', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'contacter',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(db_column='disk_id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='disk_name', max_length=30, null=True)),
                ('model', models.CharField(blank=True, db_column='disk_model', max_length=30, null=True)),
                ('raid_name', models.CharField(blank=True, max_length=100, null=True)),
                ('raid_type', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.CharField(blank=True, db_column='disk_size', max_length=30, null=True)),
                ('status', models.CharField(blank=True, db_column='disk_status', max_length=100, null=True)),
            ],
            options={
                'db_table': 'disk',
            },
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(db_column='environment_id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='environment_name', max_length=100, null=True)),
            ],
            options={
                'db_table': 'environment',
            },
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(db_column='idc_id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='idc_name', max_length=100, null=True)),
            ],
            options={
                'db_table': 'idc',
            },
        ),
        migrations.CreateModel(
            name='Nic',
            fields=[
                ('id', models.AutoField(db_column='nic_id', primary_key=True, serialize=False)),
                ('mac', models.CharField(blank=True, db_column='nic_mac', max_length=50, null=True)),
                ('model', models.CharField(blank=True, db_column='nic_model', max_length=100, null=True)),
            ],
            options={
                'db_table': 'nic',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.CharField(db_column='server_id', max_length=100, primary_key=True, serialize=False)),
                ('sn', models.CharField(blank=True, max_length=100, null=True)),
                ('cpu_model', models.CharField(blank=True, max_length=100, null=True)),
                ('cpu_sockets', models.IntegerField(blank=True, null=True)),
                ('cpu_cores', models.IntegerField(blank=True, null=True)),
                ('cpu_threads', models.IntegerField(blank=True, null=True)),
                ('mem_size', models.IntegerField(blank=True, null=True)),
                ('mem_total_slots', models.IntegerField(blank=True, null=True)),
                ('mem_free_slots', models.IntegerField(blank=True, null=True)),
                ('raid_adapter', models.CharField(blank=True, max_length=200, null=True)),
                ('raid_adapter_slot', models.CharField(blank=True, max_length=20, null=True)),
                ('ipmi_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('ipmi_user', models.CharField(blank=True, max_length=30, null=True)),
                ('ipmi_pass', models.CharField(blank=True, max_length=30, null=True)),
                ('unit', models.IntegerField(blank=True, null=True)),
                ('pxe_mac', models.CharField(blank=True, max_length=30, null=True)),
                ('pxe_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('vendor', models.CharField(blank=True, max_length=30, null=True)),
                ('model', models.CharField(blank=True, max_length=30, null=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('cabinet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='installation.Cabinet')),
                ('contacter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='installation.Contacter')),
                ('environment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='installation.Environment')),
            ],
            options={
                'ordering': ['-create_time'],
                'db_table': 'server',
            },
        ),
        migrations.CreateModel(
            name='ServerStatus',
            fields=[
                ('id', models.AutoField(db_column='server_status_id', primary_key=True, serialize=False)),
                ('status_type', models.CharField(blank=True, db_column='server_status_type', max_length=50, null=True)),
                ('name', models.CharField(blank=True, db_column='server_status_name', max_length=100, null=True)),
            ],
            options={
                'db_table': 'server_status',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(db_column='tag_id', primary_key=True, serialize=False)),
                ('tag_type', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='server',
            name='serverstatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='installation.ServerStatus'),
        ),
        migrations.AddField(
            model_name='server',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='installation.Tag'),
        ),
        migrations.AddField(
            model_name='nic',
            name='server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='installation.Server'),
        ),
        migrations.AddField(
            model_name='disk',
            name='server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='installation.Server'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='installation.Idc'),
        ),
    ]