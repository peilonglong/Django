from user import home

import django
from django.conf.urls import include, url#,patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
import xadmin
from app.pages.page_views import postview
xadmin.ROOT_PATH_NAME = 'xadmin'
settings.XADMIN_EXCLUDE_PLUGINS = ['bookmark']

xadmin.autodiscover()


#from django.contrib import admin
#admin.autodiscover()


urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^arp/', postview),

    # url(r'^app/',include('app.urls',namespace='app')),
    # url(r'^user/',include('account.urls',namespace='user')),
    url(r'^$',RedirectView.as_view(url='/xadmin/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
