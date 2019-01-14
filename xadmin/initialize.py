# coding=utf-8

from django.conf import settings
from django.utils.module_loading import module_has_submodule


def register_builtin_views(site):
    from xadmin import views
    site.register_view(r'^$', views.IndexView, name='index')
    site.register_view(r'^main.html$', views.MainView, name='main')
    site.register_view(r'^login/$', views.LoginView, name='login')
    site.register_view(r'^logout/$', views.LogoutView, name='logout')
    site.register_view(r'^settings/user$', views.UserSettingView, name='user_settings')

    site.register_modelview(r'^$', views.ListAdminView, name='%s_%s_changelist')
    site.register_modelview(r'^add/$', views.CreateAdminView, name='%s_%s_add')
    site.register_modelview(r'^(.+)/delete/$', views.DeleteAdminView, name='%s_%s_delete')
    site.register_modelview(r'^(.+)/update/$', views.UpdateAdminView, name='%s_%s_change')
    site.register_modelview(r'^(.+)/detail/$', views.DetailAdminView, name='%s_%s_detail')
    site.register_modelview(r'^(.+)/dashboard/$', views.ModelDashboard, name='%s_%s_dashboard')

    site.set_loginview(views.LoginView)

def register_builtin_plugins(site):
    from xadmin.plugins import PLUGINS
    from .dutils import import_module

    exclude_plugins = getattr(settings, 'XADMIN_EXCLUDE_PLUGINS', [])
    [import_module('xadmin.plugins.%s' % plugin) for plugin in PLUGINS if plugin not in exclude_plugins]

def autodiscover():
    import xadmin
    from xadmin.sites import site
    from .dutils import import_module

    xadmin.site = site

    # 为 crispy_form 动态设置的settings项
    setattr(settings, 'CRISPY_TEMPLATE_PACK', 'bootstrap3')
    setattr(settings, 'CRISPY_CLASS_CONVERTERS', {
        "textinput": "textinput textInput form-control",
        "fileinput": "fileinput fileUpload form-control",
        "passwordinput": "textinput textInput form-control",
    })
    # 加载内置相关视图
    register_builtin_views(site)

    # 加载插件
    register_builtin_plugins(site)

    # 加载各app的 adminx
    for app in settings.INSTALLED_APPS:
        # 加载app
        mod = import_module(app)
        if hasattr(mod,'app_label'):
            app_label = mod.app_label
        else:
            app_label = app.split('.')[-1]
        site.app_dict[app_label] = mod

        # app级菜单初始化
        default_title = hasattr(mod,'verbose_name') and u'%s 其他'%mod.verbose_name or u'其他'
        site.sys_menu[app_label] = {'_default_group':{'key': '_default_group','title': default_title, 'icon': 'fa-th-large', 'menus': []}  }
        if hasattr(mod,'menus'):
            m_menus = mod.menus
            for e in m_menus:
                site.sys_menu[app_label][e[0]] = {'key': e[0],'title': e[1], 'icon': e[2], 'menus': []}

        # 导入 adminx 模块
        try:
            before_import_registry = site.copy_registry()
            import_module('%s.adminx' % app)
        except:
            site.restore_registry(before_import_registry)
            if module_has_submodule(mod, 'adminx'):
                raise
