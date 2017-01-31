from django.contrib import admin

# Register your models here.
from .forms import SignUpData
from .models import DataRegistration
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display=["__str__","gender","batch_number","alma_mater","address","blood_gruoup","timestamp","updated"]
    form=SignUpData

admin.site.register(DataRegistration,DataAdmin)