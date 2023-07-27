from django.contrib import admin

# Register your models here.
from .models import FirstMenu, SecondMenu, NavigationSite


@admin.register(FirstMenu)
class FirstMenuAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('id', 'name', 'create_date', 'update_date', 'sort_order')
    list_editable = ('sort_order',)
    list_display_links = ('name',)
    list_filter = ('create_date', 'sort_order')
    search_fields = ['name']


@admin.register(SecondMenu)
class SecondMenuAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('id', 'name', 'create_date', 'update_date', 'father', 'sort_order')
    list_editable = ('sort_order', 'father')
    list_display_links = ('name',)
    list_filter = ('create_date', 'sort_order', 'father')
    search_fields = ['name', 'father__name']
    autocomplete_fields = ['father']


@admin.register(NavigationSite)
class NavigationSiteAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('id', 'name', 'link',
                    'create_date', 'menu', 'sort_order', 'is_show', 'not_show_reason')
    list_display_links = ('name',)
    list_filter = ('create_date', 'sort_order', 'menu')
    list_editable = ('menu', 'sort_order')
    autocomplete_fields = ['menu']
