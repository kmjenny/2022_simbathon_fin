# Generated by Django 4.0.6 on 2022-07-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0008_freepost_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freepost',
            name='mode',
            field=models.CharField(choices=[('팝니다', '팝니다'), ('삽니다', '삽니다')], default='삽니다', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='count',
            field=models.CharField(choices=[('상관없음', '상관없음'), ('1명', '1명'), ('2명', '2명'), ('3명', '3명'), ('4명', '4명'), ('5명 이상', '5명 이상')], default='상관없음', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='gender',
            field=models.CharField(choices=[('상관없음', '상관없음'), ('남자', '남자'), ('여자', '여자')], default='상관없음', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.CharField(choices=[('자유', '자유'), ('전공', '전공')], default='자유', max_length=100),
        ),
    ]