# coding=utf-8
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt
from requests import request
from xadmin.sites import site
from app.model.cms_models import Record
import xadmin
from xadmin.views.page import PageView

# class TestPage(PageView):
#     '''
#     带ajax页链接
#     '''
#     verbose_name = u'ARP欺骗'
#     app_label = 'app'
#     menu_group = 'arp_group'
#     template = 'arp.html'
    # def get_media(self):
    #     media = self.vendor('plugin.quick-form.js', 'form.css')
    #     return media
    #
    # def get_content(self):
    #     return mark_safe('<a data-refresh-url="/xadmin/page/testpage2/" href="/xadmin/page/formpage1" class="ajaxform-handler" title="测试AjaxForm">GO</a>')
# site.register_page(TestPage)

class TestPage1(PageView):
    '''
    基本page页
    '''
    verbose_name = u'ARP欺骗(Schneider)'
    app_label = 'app'
    menu_group = 'arp_group'
    icon = "fa fa-circle"
    template = 'arpschne.html'

site.register_page(TestPage1)

@csrf_exempt
def postview(request):
    name = request.POST.get('name')
    start= request.POST.get('start')
    print name
    print start
    print ("***********")
    Record.objects.create(name=name,start=start)
    return JsonResponse({'data': 'ok'} )


class TestPage2(PageView):
    verbose_name = u'ARP欺骗(Siemens)'
    app_label = 'app'
    menu_group = 'arp_group'
    icon = "fa fa-circle"
    template = 'arpsiem.html'

site.register_page(TestPage2)

class TestPage3(PageView):
    verbose_name = u'ARP欺骗(RTU)'
    app_label = 'app'
    menu_group = 'arp_group'
    icon = "fa fa-circle"
    template = 'arprut.html'

site.register_page(TestPage3)


class TestPage41(PageView):
    verbose_name = u'DOS攻击(Schneider)'
    app_label = 'app'
    menu_group = 'dos_group'
    icon = "fa fa-circle"
    template = 'dosschne.html'

    def get_content(self):
        return 'OK'
site.register_page(TestPage41)

class TestPage42(PageView):
    verbose_name = u'DOS攻击(Siemens)'
    app_label = 'app'
    menu_group = 'dos_group'
    icon = "fa fa-circle"
    template = 'dossiem.html'

    def get_content(self):
        return 'OK'
site.register_page(TestPage42)


class TestPage43(PageView):
    verbose_name = u'DOS攻击(RTU)'
    app_label = 'app'
    menu_group = 'dos_group'
    icon = "fa fa-circle"
    template = 'dosrut.html'

    def get_content(self):
        return 'OK'
site.register_page(TestPage43)

class TestPage51(PageView):
    verbose_name = u'指令注入(Schneider)'
    app_label = 'app'
    menu_group = 'zhu_group'
    icon = "fa fa-circle"
    template = 'zhuschne.html'

    def get_content(self):
        return 'OK'
site.register_page(TestPage51)

class TestPage52(PageView):
    verbose_name = u'指令注入(Siemens)'
    app_label = 'app'
    menu_group = 'zhu_group'
    icon = "fa fa-circle"
    template = 'zhusiem.html'

    def get_content(self):
        return 'OK'
site.register_page(TestPage52)

class TestPage53(PageView):
    verbose_name = u'指令注入(RTU)'
    app_label = 'app'
    menu_group = 'zhu_group'
    icon = "fa fa-circle"
    template = 'zhurut.html'

    def get_content(self):
        return 'OK'
site.register_page(TestPage53)



class TestPage61(PageView):
    verbose_name = u'数据篡改(Schneider)'
    app_label = 'app'
    menu_group = 'shu_group'
    icon = "fa fa-circle"
    template = 'shuschne.html'

    def get_content(self):
        return 'OK'
site.register_page(TestPage61)

class TestPage62(PageView):
    verbose_name = u'数据篡改(Siemens)'
    app_label = 'app'
    menu_group = 'shu_group'
    icon = "fa fa-circle"
    template = 'shusiem.html'

    def get_content(self):
        return 'OK'
site.register_page(TestPage62)


class TestPage63(PageView):
    verbose_name = u'数据篡改(RTU)'
    app_label = 'app'
    menu_group = 'shu_group'
    icon = "fa fa-circle"
    template = 'shurtu.html'

    def get_content(self):
        return 'OK'
site.register_page(TestPage63)

class TestPage71(PageView):
    '''
    基本page页
    '''
    verbose_name = u'U盘攻击'
    app_label = 'app'
    menu_group = 'pan_group'
    icon = "fa fa-circle"
    template = 'upan.html'
    def get_content(self):
        return 'OK'
site.register_page(TestPage71)

class TestPage72(PageView):
    '''
    基本page页
    '''
    verbose_name = u'GPS攻击'
    app_label = 'app'
    menu_group = 'pan_group'
    icon = "fa fa-circle"
    template = 'gps.html'
    def get_content(self):
        return 'OK'
site.register_page(TestPage72)

class TestPage73(PageView):
    '''
    基本page页
    '''
    verbose_name = u'无线攻击'
    app_label = 'app'
    menu_group = 'pan_group'
    icon = "fa fa-circle"
    template = 'wifi.html'
    def get_content(self):
        return 'OK'
site.register_page(TestPage73)
