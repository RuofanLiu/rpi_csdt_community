# -*- coding: utf-8 -*-

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_share', '0002_auto_20141219_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='classroom',
            field=models.ForeignKey(related_name='+', blank=True, to='project_share.Classroom', null=True),
            preserve_default=True,
        ),
    ]
