from django.db import models
from django.utils.html import mark_safe
from django.urls import reverse
from  ckeditor.fields import RichTextField 
from cloudinary.models import CloudinaryField

class Product(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    image = CloudinaryField('Products')
    slug = models.CharField(max_length=400)
    size = models.CharField(max_length=400)
    detail = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=True)
 
    class Meta:
        verbose_name_plural= '1. Products'
    
    def Product_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))

    def __str__(self):
        return self.title


class blog(models.Model):
    title = models.CharField(max_length = 150)
    overview =  RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumnail = CloudinaryField('blog')
    date_added = models.DateField('date published',auto_now_add=True)
   
      
       
    def __str__(self):
        return self.title
    


    class Meta:
        ordering = ['-id']
        verbose_name_plural= '4. Blogs'
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={
            'id': self.id
        })


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100 )
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    amount_to_pay = models.DecimalField(max_digits=8, decimal_places=2)


    class Meta:
        verbose_name_plural= '2. Orders'
        ordering = ['-created_at']
    
    def __str__(self):
        return 'Order N°'+str(self.id) +' / '+ 'Client: '+ self.first_name + ' ' + self.last_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return 'Order N°'+str(self.order.id) +' / '+ 'Client: '+ str(self.order.first_name) + ' ' + str(self.order.last_name)
    
    def get_total_price(self):
        return self.price * self.quantity
    
    class Meta:
        verbose_name_plural= '3. Order Items'


class Contact (models.Model):
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)

    
    class Meta:
        verbose_name_plural= '5. Contacts'
  
    def __str__(self):
        return self.name


class subcriber (models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural= '6. Subcribers'

class testimonial(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    image = CloudinaryField('testimonials')
    detail = detail = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= '7. Testimonials'




class banner(models.Model):
    image = CloudinaryField('banners')
    title_1 = models.CharField(max_length=600)
    title_2 = models.CharField(max_length=600)

    def __str__(self):
        return self.title_1

    class Meta:
        verbose_name_plural= '8. Banners'