#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    create_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

    #python2使用__unicode__, python3使用__str__
    def __unicode__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-create_time']