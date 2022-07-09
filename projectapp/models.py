import imp
from django.db import models
from django.conf import settings 
from accounts.models import User

GENDER_CHOICES = [
        ('상관없음', '상관없음'),
        ('남자', '남자'),
        ('여자', '여자'),
]

TOPIC_CHOICES = [
        ('자유', '자유'),
        ('전공', '전공'),
]

COUNT_CHOICES = [
        ('1명', '1명'),
        ('2명', '2명'),
        ('3명', '3명'),
        ('4명', '4명'),
        ('5명 이상', '5명 이상'),
]

MODE_CHOICES = [
        ('팝니다', '팝니다'),
        ('삽니다', '삽니다'),
]


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length= 100, choices=GENDER_CHOICES, default='상관없음')
    topic = models.CharField(max_length= 100, choices=TOPIC_CHOICES, default='자유')
    count = models.CharField(max_length= 100, choices=COUNT_CHOICES, default='1명')


    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    author = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class FreePost(models.Model):
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default= 0)
    image = models.ImageField(upload_to = "post/", blank=True, null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, blank=True, null=True)


    mode = models.CharField(max_length= 100, choices=MODE_CHOICES, default='삽니다')

    def __str__(self):
        return self.title

class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment