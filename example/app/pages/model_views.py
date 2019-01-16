# coding=utf-8
from xadmin.sites import site

import xadmin
from xadmin.views import ModelAdminView


class TestModelAdminView(ModelAdminView):

    def get(self, request, obj_id):
        return self.render_text('OK')

site.register_modelview(r'^(.+)/test/$', TestModelAdminView, name='%s_%s_test')
