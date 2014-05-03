from django.contrib import admin
from sllod.models import Poll, Option

# Register your models here.
class OptionInline(admin.TabularInline):
    model = Option
    extra = 3
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['message']}),
        ('Date information', {'fields': ['created_at'], 'classes': ['collapse']}),
    ]
    inlines = [OptionInline]
    list_display = ('message', 'created_at', 'was_published_recently')
    list_filter = ['created_at']
    search_fields = ['message']


    
admin.site.register(Poll, PollAdmin)
#class OptionAdmin(admin.ModelAdmin):
#    fields = ['option_text', 'votes']
#admin.site.register(Option, OptionAdmin)
#admin.site.register(Option)