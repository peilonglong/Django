# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-14 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import xadmin.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            bases=(models.Model, xadmin.models.ExtModel),
        ),
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user_count', models.IntegerField()),
                ('view_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Access Record',
                'verbose_name_plural': 'Access Record',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('date', models.DateField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('content', models.TextField(blank=True, null=True, verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            bases=(models.Model, xadmin.models.ExtModel),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u540d\u79f0')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.Category', verbose_name='\u7236\u7c7b\u522b')),
            ],
            options={
                'verbose_name': '\u7c7b\u522b',
                'verbose_name_plural': '\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('nagios_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Nagios Host ID')),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('internal_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('user', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=128)),
                ('ssh_port', models.IntegerField(blank=True, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Normal'), (1, 'Down'), (2, 'No Connect'), (3, 'Error')])),
                ('brand', models.CharField(choices=[('DELL', 'DELL'), ('HP', 'HP'), ('Other', 'Other')], max_length=64)),
                ('model', models.CharField(blank=True, default=b'', max_length=64, null=True)),
                ('cpu', models.CharField(max_length=64)),
                ('core_num', models.SmallIntegerField(choices=[(2, b'2 Cores'), (4, b'4 Cores'), (6, b'6 Cores'), (8, b'8 Cores'), (10, b'10 Cores'), (12, b'12 Cores'), (14, b'14 Cores'), (16, b'16 Cores'), (18, b'18 Cores'), (20, b'20 Cores'), (22, b'22 Cores'), (24, b'24 Cores'), (26, b'26 Cores'), (28, b'28 Cores')])),
                ('hard_disk', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('system', models.CharField(choices=[('CentOS', 'CentOS'), ('FreeBSD', 'FreeBSD'), ('Ubuntu', 'Ubuntu')], max_length=32, verbose_name='System OS')),
                ('system_version', models.CharField(max_length=32)),
                ('system_arch', models.CharField(choices=[('x86_64', 'x86_64'), ('i386', 'i386')], max_length=32)),
                ('create_time', models.DateField()),
                ('guarantee_date', models.DateField()),
                ('service_type', models.CharField(choices=[(b'moniter', 'Moniter'), (b'lvs', 'LVS'), (b'db', 'Database'), (b'analysis', 'Analysis'), (b'admin', 'Admin'), (b'storge', 'Storge'), (b'web', 'WEB'), (b'email', 'Email'), (b'mix', 'Mix')], max_length=32)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Host',
                'verbose_name_plural': 'Host',
            },
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('hosts', models.ManyToManyField(related_name='groups', to='app.Host', verbose_name='Hosts')),
            ],
            options={
                'verbose_name': 'Host Group',
                'verbose_name_plural': 'Host Group',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('contact', models.CharField(max_length=32)),
                ('telphone', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
                ('customer_id', models.CharField(max_length=128)),
                ('create_time', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'IDC',
                'verbose_name_plural': 'IDC',
            },
        ),
        migrations.CreateModel(
            name='MaintainLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintain_type', models.CharField(max_length=32)),
                ('hard_type', models.CharField(max_length=16)),
                ('time', models.DateTimeField()),
                ('operator', models.CharField(max_length=16)),
                ('note', models.TextField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Host')),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.IDC')),
            ],
            options={
                'verbose_name': 'Maintain Log',
                'verbose_name_plural': 'Maintain Log',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.IDC'),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='app.Category', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x88\x86\xe7\xb1\xbb'),
        ),
        migrations.AddField(
            model_name='a',
            name='b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.B', verbose_name=b'\xe5\xb1\x9e\xe4\xb8\xbb'),
        ),
    ]
