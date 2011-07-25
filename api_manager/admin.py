
from api_manager.models import *
from django.contrib import admin


class KeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'key_user', 'active')
    
    actions = ['activate_keys', 'de_activate_key']
    
    def activate_keys(self, request, queryset):
        rows = queryset.update(active=True)
        if rows == 1:
            msg = "1 key was"
        else:
            msg = "%s keys were" % rows
        self.message_user(request, "%s successfully activated." % msg)
        
    def de_activate_keys(self, request, queryset):
        rows = queryset.update(active=False)
        if rows == 1:
            msg = "1 key was"
        else:
            msg = "%s keys were" % rows
        self.message_user(request, "%s successfully de-activated." % msg)
        
class KeyUsageAdmin(admin.ModelAdmin):
    list_display = ('log_message', 'key_user')
    
    def key_user(self, obj):
        return obj.key.key_user

admin.site.register(Keys, KeyAdmin)
admin.site.register(KeyUsage, KeyUsageAdmin)