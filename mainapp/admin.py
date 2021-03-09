from django.contrib import admin
from .models import *

class Personal(admin.ModelAdmin):
    list_display = ('name', 'email')

class Social(admin.ModelAdmin):
    list_display = ('facebook', 'twitter')

class Web(admin.ModelAdmin):
    list_display = ('title', 'profile')

class Skills(admin.ModelAdmin):
    list_display = ('html', 'css', 'php', 'wordpress', 'android')

class Testimonials(admin.ModelAdmin):
    list_display = ('name', 'role')

class Facts(admin.ModelAdmin):
    list_display = ('projects', 'clients')

class Cat(admin.ModelAdmin):
    list_display = ('id', 'title')

class Port(admin.ModelAdmin):
    list_display = ('name', 'category', 'image')
    def category(self, instance):
        return instance.Category.title

admin.site.register(PersonalInformation, Personal)
admin.site.register(SocialMediaLinks, Social)
admin.site.register(Website, Web)
admin.site.register(Skill, Skills)
admin.site.register(Fact, Facts)
admin.site.register(Testimonial, Testimonials)
admin.site.register(Resume)
admin.site.register(Category, Cat)
admin.site.register(Portfolio, Port)
