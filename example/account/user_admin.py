import xadmin
from .models import user_profile as UserProfile

class UserProfileadmin(object):
    list_display = ('name', 'start', 'create_time')
xadmin.site.register(UserProfile,UserProfileadmin)