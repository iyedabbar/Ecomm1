from django.contrib import admin
from .models import *

admin.site.site_header = 'Retatse'
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' , 'status' , 'is_featured' , 'price' , 'Product_image' )
    list_editable = ('status','is_featured')
admin.site.register(Product,ProductAdmin)
admin.site.register(blog)
admin.site.register(Order)

class ProductInOrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]

    class Meta:
        model = OrderItem

admin.site.register(OrderItem, ProductInOrderAdmin)

admin.site.register(subcriber)
admin.site.register(Contact)
admin.site.register(testimonial)
admin.site.register(banner)

