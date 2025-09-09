from django.contrib import admin
from django.utils.html import format_html
from .models import *

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'preview')
    search_fields = ('title', 'description')
    list_display_links = ('title',)

    # Short description for admin list
    def short_description(self, obj):
        if obj.description:
            return obj.description if len(obj.description) <= 60 else obj.description[:57] + "..."
        return ""
    short_description.short_description = 'Description'

    # Image preview in admin
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px; width:auto; object-fit:cover; border-radius:4px;" />',
                obj.image.url
            )
        return "(No image)"
    preview.short_description = 'Preview'




class UspAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    search_fields = ('title', 'description')
    list_display_links = ('title',)



class EmergencySectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    search_fields = ('title', 'description')
    list_display_links = ('title',)





class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'Mission', 'Vission')
    list_display_links = ('id',)
    search_fields = ('Title', 'Mission', 'Vission')
    list_filter = ('Mission',)
    ordering = ('-id',)




class Why_ChooseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    search_fields = ('title', 'description')
    list_display_links = ('title',)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    search_fields = ('title', 'description')
    list_display_links = ('title',)


class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    search_fields = ('title', 'description')
    list_display_links = ('title',)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    search_fields = ('title', 'description')
    list_display_links = ('title',)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'department',)
    search_fields = ('title', 'department','twitter','facebook','instagram','linkedin')
    list_display_links = ('title',)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview')

    # Short description for admin list
    def short_description(self, obj):
        if obj.description:
            return obj.description if len(obj.description) <= 60 else obj.description[:57] + "..."
        return ""

    # Image preview in admin
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px; width:auto; object-fit:cover; border-radius:4px;" />',
                obj.image.url
            )
        return "(No image)"
    preview.short_description = 'Preview'



class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'Question', 'Answer',)
    search_fields = ('Question', 'Answer')
    list_display_links = ('Question',)


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'update_at']






admin.site.register(EmergencySection,EmergencySectionAdmin)
admin.site.register(Departments,DepartmentsAdmin)
admin.site.register(Why_Choose,Why_ChooseAdmin)
admin.site.register(Services,ServicesAdmin)
admin.site.register(Setting,SettingAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(FAQ,FAQAdmin)
admin.site.register(Usp,UspAdmin)