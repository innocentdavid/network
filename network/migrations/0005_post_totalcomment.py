# Generated by Django 3.0.6 on 2020-07-28 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20200728_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='totalComment',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
