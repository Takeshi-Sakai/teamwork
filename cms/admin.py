from django.contrib import admin
from cms.models import Improvement, Hh

# Register your models here.

class ImprovementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'done_date', 'boss_confirmation')
    list_display_links = ('id', 'name')
admin.site.register(Improvement, ImprovementAdmin)

class HhAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')
    list_display_links = ('id', 'comment')
admin.site.register(Hh, HhAdmin)