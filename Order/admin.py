from django.contrib import admin

# Register your models here.

from .models import *

class OrderAdmin(admin.ModelAdmin): 
    
    def save_model(self, request, obj, form, change):
        update_fields = []
        for key, value in form.cleaned_data.items():
            # True if something changed in model
            if value != form.initial[key]:
                update_fields.append(key)

        obj.save(update_fields=update_fields)


admin.site.register(Order, OrderAdmin)
admin.site.register(Pizza)
