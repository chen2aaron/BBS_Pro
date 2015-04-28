# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20150417_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='content',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bbs',
            name='ranking',
            field=models.IntegerField(verbose_name=b'\xe7\x83\xad\xe5\xba\xa6'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bbs',
            name='summary',
            field=models.CharField(max_length=256, null=True, verbose_name=b'\xe6\xa6\x82\xe8\xa6\x81', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bbs',
            name='title',
            field=models.CharField(max_length=64, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bbs',
            name='view_count',
            field=models.IntegerField(verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f'),
            preserve_default=True,
        ),
    ]
