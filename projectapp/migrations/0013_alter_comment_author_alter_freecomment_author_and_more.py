# Generated by Django 4.0.6 on 2022-07-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0012_comment_author_freecomment_author_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='freecomment',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='freepost',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
