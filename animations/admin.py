from django.contrib import admin
from .models import Contacts
from .models import Register
from .models import News


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number','address','message')


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number','password')


class NewsAdmin(admin.ModelAdmin):
    list_display =  ('email','email')


admin.site.register(Contacts,ContactsAdmin)
admin.site.register(Register,RegisterAdmin)
admin.site.register(News,NewsAdmin)
