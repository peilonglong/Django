# coding=utf-8
from django.shortcuts import render
from django.utils.safestring import mark_safe
from requests import request
from . import funtion as post
import xadmin
from xadmin.views.page import PageView

class TestPage(PageView):
    '''
    带ajax页链接
    '''
    verbose_name = u'ARP欺骗'
    app_label = 'app'
    menu_group = 'test_group'
    template = 'arp.html'
    # def get_media(self):
    #     media = self.vendor('xadmin.plugin.quick-form.js', 'xadmin.form.css')
    #     return media
    #
    # def get_content(self):
    #     return mark_safe('<a data-refresh-url="/xadmin/page/testpage2/" href="/xadmin/page/formpage1" class="ajaxform-handler" title="测试AjaxForm">GO</a>')
xadmin.site.register_page(TestPage)

class TestPage1(PageView):
    '''
    基本page页
    '''
    verbose_name = u'ARP欺骗(Schneider)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'arpschne.html'

    def post1(self):
        print 'jihu'
        return render(request, 'arpschne.html', locals())

xadmin.site.register_page(TestPage1)

class TestPage2(PageView):
    verbose_name = u'ARP欺骗(Siemens)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'arpsiem.html'

xadmin.site.register_page(TestPage2)

class TestPage3(PageView):
    verbose_name = u'ARP欺骗(RTU)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'arprut.html'

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage3)

class TestPage3(PageView):
    '''
    bootstrap常用html
    '''
    verbose_name = u'DOS攻击'
    app_label = 'app'
    menu_group = 'test_group'
    template = 'dos.html'

xadmin.site.register_page(TestPage3)

class TestPage31(PageView):
    verbose_name = u'DOS攻击(Schneider)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'dosschne.html'

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage31)

class TestPage32(PageView):
    verbose_name = u'DOS攻击(Siemens)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'dossiem.html'

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage32)

class TestPage33(PageView):
    verbose_name = u'DOS攻击(RTU)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'dosrut.html'

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage33)


class TestPage4(PageView):
    '''
    bootstrap常用html
    '''
    verbose_name = u'指令注入'
    app_label = 'app'
    menu_group = 'test_group'
    template = 'zhu.html'

xadmin.site.register_page(TestPage4)


class TestPage41(PageView):
    verbose_name = u'指令注入(Schneider)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'zhuschne.html'

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage41)

class TestPage42(PageView):
    verbose_name = u'指令注入(Siemens)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'zhusiem.html'

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage42)

class TestPage43(PageView):
    verbose_name = u'指令注入(RTU)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'zhurut.html'

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage43)

class TestPage5(PageView):

    verbose_name = u'数据篡改'
    app_label = 'app'
    menu_group = 'test_group'
    template = 'bootstrap.html'

xadmin.site.register_page(TestPage5)

class TestPage41(PageView):
    verbose_name = u'数据篡改(Schneider)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'zhuschne.html'

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage41)

class TestPage41(PageView):
    verbose_name = u'数据篡改(Siemens)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'zhuschne.html'

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage41)


class TestPage43(PageView):
    verbose_name = u'数据篡改(RTU)'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"
    template = 'zhurut.html'

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage43)






class TestPage6(PageView):
    '''
    bootstrap常用html
    '''
    verbose_name = u'非法攻击'
    app_label = 'app'
    menu_group = 'test_group'
    template = 'bootstrap.html'

xadmin.site.register_page(TestPage6)


class TestPage1(PageView):
    '''
    基本page页
    '''
    verbose_name = u'U盘攻击'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage1)

class TestPage8(PageView):
    '''
    基本page页
    '''
    verbose_name = u'GPS攻击'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage8)

class TestPage7(PageView):
    '''
    基本page页
    '''
    verbose_name = u'无线攻击'
    app_label = 'app'
    menu_group = 'test_group'
    icon = "fa fa-circle"

    def get_content(self):
        return 'OK'
xadmin.site.register_page(TestPage7)
