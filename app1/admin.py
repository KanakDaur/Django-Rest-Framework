from django.contrib import admin
from app1.models import Product
# Register your models here.

admin.site.register(Product)
admin.site.site_header = "django REST Framework"
