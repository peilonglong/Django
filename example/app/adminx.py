# -*- coding: utf-8 -*-

import xadmin
from xadmin import site
from xadmin import views
from xadmin.views.dashboard import AppDashboard

from app import models


### 全局变量设置 ###
xadmin.site.site_title = '健信科技后台管理'
xadmin.site.site_footer = 'MYRTSEC'
xadmin.site.head_fix = False
xadmin.site.ext_ui = True
#xadmin.site.menu_style = 'default'


### 公共类默认值设置 ###
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = False
site.register(views.BaseView, BaseSetting)

class GlobalSetting(object):
    global_search_models = [models.Host, models.IDC]
site.register(views.SiteView, GlobalSetting)


from . import dashboard
from . import admins
from . import pages
