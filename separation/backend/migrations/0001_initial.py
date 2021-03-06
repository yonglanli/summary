# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-12 12:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID', primary_key=True, serialize=False, verbose_name='UUID')),
                ('name_cn', models.CharField(help_text='中文名称', max_length=1000, verbose_name='中文名称')),
                ('name_en', models.CharField(help_text='英文名称', max_length=1000, verbose_name='英文名称')),
                ('source', models.CharField(help_text='还不知道是啥', max_length=1000, verbose_name='还不知道是啥')),
                ('isDelete', models.BooleanField(db_column='isdelete', default=False, help_text='是否已删除（是，否）', verbose_name='是否已删除（是，否）')),
            ],
            options={
                'verbose_name': '关键词表',
                'verbose_name_plural': '关键词表',
                'db_table': 'md_keyword',
            },
        ),
        migrations.CreateModel(
            name='KeyWordType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID', primary_key=True, serialize=False, verbose_name='UUID')),
                ('typename', models.CharField(help_text='类型名称', max_length=50, verbose_name='类型名称')),
                ('isDelete', models.BooleanField(db_column='isdelete', default=False, help_text='是否已删除（是，否）', verbose_name='是否已删除（是，否）')),
                ('modifytime', models.DateTimeField(blank=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('createtime', models.DateTimeField(blank=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('createuser', models.ForeignKey(blank=True, db_column='createuser', help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Md_keywordtype_createuserid', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('modifyuser', models.ForeignKey(blank=True, db_column='modifyuser', help_text='修改人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Md_keywordtype_modifyuserid', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
            ],
            options={
                'verbose_name': '关键词类型表',
                'verbose_name_plural': '关键词类型表',
                'db_table': 'md_keyword_type',
            },
        ),
        migrations.AddField(
            model_name='keyword',
            name='kw_type',
            field=models.ForeignKey(blank=True, db_column='kw_type', help_text='关键字类型', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Md_keyword_kw_type', to='backend.KeyWordType', verbose_name='关键字类型'),
        ),
    ]
