from django.contrib import admin
from .models import *
from django.utils.html import format_html


@admin.register(ProjectContact)
class ProjectContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'text')
    list_filter = ('name',)

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'description', 'display_img')

    def display_img(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 10px;" />', obj.img.url)
        return "<code>Нет изображения</code>"
    display_img.short_description = 'Изображение'


@admin.register(Progect)
class ProgectAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_img')
    search_fields = ('title',)

    def display_img(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 10px;" />', obj.img.url)
        return "<code>Нет изображения</code>"
    display_img.short_description = 'Изображение'


@admin.register(Comands)
class ComandsAdmin(admin.ModelAdmin):
    list_display = ('name', 'positon', 'display_img')
    search_fields = ('name', 'positon')

    def display_img(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 10px;" />', obj.img.url)
        return "<code>Нет изображения</code>"
    display_img.short_description = 'Изображение'


@admin.register(SchoolContact)
class SchoolContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'text')
    list_filter = ('name','phone_number')


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'discount', 'launch')
    search_fields = ('name', 'title')
    list_filter = ('launch',)


@admin.register(Pros)
class ProsAdmin(admin.ModelAdmin):
    readonly_fields = ["display_img"]
    list_display = ('trainees', 'mentors', 'graduates', 'display_img') 
    fieldsets = [
        (
            "Преимущества",
            {
                "fields": ["trainees", "mentors", "graduates"],
            },
        ),
        (
            "Подарки от компании",
            {
                "classes": ["collapse"],
                "fields": ["title", "description", "img", "display_img"],  
            },
        ),
    ]

    def display_img(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 10px;" />', obj.img.url)
        return format_html("<code>Нет изображения</code>")

    display_img.short_description = 'Изображение'


@admin.register(Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'display_img')

    def display_img(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 10px;" />', obj.img.url)
        return "<code>Нет изображения</code>"
    display_img.short_description = 'Изображение'