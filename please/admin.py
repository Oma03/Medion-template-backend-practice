from django.contrib import admin
from .models import Medicine, Vitamins, Contacts, New, Log


# Register your models here.
admin.site.register(Medicine)
admin.site.register(Vitamins)
admin.site.register(Contacts)
admin.site.register(Log)
admin.site.register(New)
