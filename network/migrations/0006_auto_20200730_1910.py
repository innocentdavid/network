# Generated by Django 3.0.6 on 2020-07-30 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_post_totalcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='totalComment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='totalDislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='totalFollower',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='totalLikes',
            field=models.IntegerField(default=0),
        ),
    ]
