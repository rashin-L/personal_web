from django.contrib import admin
from .models import introduction, contact, socialMedia



@admin.register(introduction)
class introductionAdmin(admin.ModelAdmin):    
    list_display = ('first_name','last_name','description', 'main_img', 'logo', 'cv', 'update_date', 'is_active')
    list_editable = ['is_active', ]
    search_fields = ['first_name', ]
    
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):    
    list_display = ('first_name','last_name', 'subject', 'message', 'email', 'is_seen', 'register_date')
    list_editable = ['is_seen', ]
    search_fields = ['subject', ] 


@admin.register(socialMedia)
class socialMediaAdmin(admin.ModelAdmin):    
    list_display = ('email','linkedin','gitHub', 'update_date', 'is_active',)
    list_editable = ['is_active', ]
    search_fields = ['email', ]  