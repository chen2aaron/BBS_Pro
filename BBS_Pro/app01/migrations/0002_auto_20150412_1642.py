# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bbs',
            old_name='titile',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='photo',
            field=models.ImageField(default=b'upload_imgs/user-1.jpg', null=True, upload_to=b'upload_imgs/', blank=True),
            preserve_default=True,
        ),
    ]
