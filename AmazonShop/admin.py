from django.contrib import admin
from .models import AffiliateModeSite
from . import models

# Register your models here.
app_name = 'AmazonShop'
class AffiliateAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title",]}
    list_display = ['title','offer','content','price']
    
admin.site.register(AffiliateModeSite, AffiliateAdmin)