'''
音乐 视频 图片 文章 时间 作者 地域  其他文章链接 （赞 浏览数） 评论 转发 tag footnote
'''




from django.db import models
from django.utils import timezone
import pytz


class TimezoneMiddleware(object):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()

class attach(models.Model):
    like_or_dislike=(
        ('like'),
        ('dislike'),
        )
    favour = models.CharField(max_length=1, choices=like_or_dislike)
    transmit = 
    view = 
    tag = 


class author_information(models.Model):
    author_first_name = models.CharField(max_length=50)
    author_last_name = models.CharField(max_length=50)
    pub_place = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

class article(models.Model):
    inital_inf = "This article has not been found"
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    def __init__(self, arg):
        return self.inital_inf

class picture(models.Model):
    inital_inf = "This picture has not been found"
    category = models.CharField(max_length=200)
    place_took = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    def __init__(self, arg):
        return self.inital_inf

class vedio(models.Model):
    inital_inf = "This vedio has not been found"
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    def __init__(self, arg):
        return self.inital_inf
