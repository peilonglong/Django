# coding=utf-8
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name='profile')
    mobile = models.CharField('手机号', max_length=64, blank=True, null=True)
    #image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png")
    # record = models.ForeignKey('Record', on_delete=models.CASCADE)
    class Meta:
        app_label ='auth'
        db_table = 'auth_userprofile'
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

#
# #记录表
# class Record(models.Model):
#     admin_record =(
#         (0,'恢复'),
#         (1,'启动')
#     )
#     name = models.CharField(max_length=60,verbose_name='攻击名称')
#     start = models.SmallIntegerField(choices=admin_record,default='',verbose_name='攻击的状态')
#     create_time = models.DateField(max_length=50,verbose_name='攻击时间')
#
#     class Meta:
#         app_label ='auth'
#         db_table = 'record'
#         verbose_name = u'纪录'
#         verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    SEND_TYPE_CHOICE = (
        ('register', u'register'),
        ('forget', u'forget')
    )
    code = models.CharField(max_length=20, verbose_name=u'code')
    email = models.EmailField(max_length=50, verbose_name=u'email')
    send_type = models.CharField(max_length=10, choices=SEND_TYPE_CHOICE, default='forget')
    send_time = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

    class Meta:
        app_label ='account'
        verbose_name = u'Email验证码'
        verbose_name_plural = verbose_name
