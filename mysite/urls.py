"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from main.views import *


urlpatterns = [ path('jet/', include('jet.urls', 'jet')),
                path('retasteadmin/', admin.site.urls),
                path( '', home),
                path('home/', home),
                path('shop/', shop),
                path('blog/', Blog),
                path('blog_detail/<id>/', blog_detail , name ='blog-detail'),
                path('product/<str:slug>/<int:id>',product,name='product'),
                path('cart_detail/',cart_detail,name='cart'),
                path('success/',success,name='success'),
                path('contact/',contact,name='contact'),
                path('about/',about,name='about'),
                path('search/',search,name='search'),
            
             
               
               

                
                ]
                





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
