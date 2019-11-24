from django.contrib import admin
from .models import UserProfile


# Register your models here.


from .models import inih, menu, servh,archivo,habh
class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)    
admin.site.register(inih)
admin.site.register(menu)
admin.site.register(servh)
admin.site.register(archivo)
admin.site.register(habh)
