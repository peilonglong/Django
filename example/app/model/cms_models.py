# coding=utf-8

from django.db import models

class Category(models.Model):
    name = models.CharField(u"名称", max_length=64)
    parent = models.ForeignKey('self', verbose_name=u'父类别', related_name='children', null=True, blank=True)

    class Meta:
        app_label = 'app'
        verbose_name=u'类别'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(u"标题", max_length=200)
    date = models.DateField(u"发布时间")
    content = models.TextField(u"内容", null=True, blank=True)
    categories = models.ManyToManyField('Category', verbose_name='所属分类', null=True, blank=True)

    class Meta:
        app_label = 'app'
        verbose_name=u'文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


#记录表
class Records(models.Model):
    admin_record =(
        (0,'恢复'),
        (1,'启动')
    )
    name = models.CharField(max_length=60,verbose_name='攻击名称')
    start = models.SmallIntegerField(choices=admin_record,default='',verbose_name='攻击的状态')
    create_time = models.DateField(max_length=50,verbose_name='攻击时间')

    class Meta:
        app_label = "app"
        db_table = 'records'
        verbose_name = u'纪录'
        verbose_name_plural = verbose_name
        permissions = (
            ("scan_records", u"查看记录"),
        )



