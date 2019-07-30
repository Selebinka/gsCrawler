from django.contrib import admin
from main.models import GoogleResultModel

class GoogleResultAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'keywords')
    list_filter = ('date', 'keywords')


admin.site.register(GoogleResultModel, GoogleResultAdmin)

