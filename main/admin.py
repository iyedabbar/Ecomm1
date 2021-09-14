from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' , 'status' , 'is_featured' , 'price' , 'Product_image' )
    list_editable = ('status','is_featured')
admin.site.register(Product,ProductAdmin)
admin.site.register(blog)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(subcriber)
admin.site.register(Contact)
admin.site.register(testimonial)

