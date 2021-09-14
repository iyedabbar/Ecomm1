from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .models import *
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.conf import settings
from .cart import Cart
from .forms import AddToCartForm,CheckoutForm
from django.contrib import messages
from .utilities import checkout,notify_customer


def home(request):
	data_1= banner.objects.all()
	data = Product.objects.filter(is_featured =True).order_by('-id')
	test = testimonial.objects.all()
	cart = Cart(request)
	if request.method == 'POST':
		form = AddToCartForm(request.POST)
		if form.is_valid():	
			quantity = form.cleaned_data['quantity']
			prod_id= request.POST.get('prod_id')
			cart.add(product_id=prod_id, quantity=quantity, update_quantity=True)
			
			messages.success(request, 'Produit ajouter au Panier')
			return redirect('/')
	else:
		form = AddToCartForm()

	if request.method=="POST":
		sub = subcriber()
		email=request.POST.get('mail')
		sub.email=email
		sub.save()
		messages.success(request, 'Produit ajouter au Panier')
		return redirect('/')
	else:
		return render(request,'index.html',{'data':data, 'form': form , 'test' :test , 'data_1':data_1 } )


def product(request,slug,id):
	cart = Cart(request)
	product=Product.objects.get(id=id)

	if request.method == 'POST':
		form = AddToCartForm(request.POST)
		if form.is_valid():
			quantity = form.cleaned_data['quantity']
			prod_id= request.POST.get('prod_id')
			cart.add(product_id=prod_id , quantity=quantity , update_quantity=True)
			messages.success(request , 'Produit ajouter au Panier')

			return redirect('product',slug=slug,id=id)
	else:
		form = AddToCartForm()

	
	related_products=Product.objects.exclude(id=id)[:4]
	return render(request, 'product-single.html',{'data':product,'related':related_products,'form': form})


def Blog(request):
	featured = blog.objects.all().order_by('-id')
	latest = blog.objects.order_by('-timestamp')[0:6]
	last = blog.objects.order_by('-timestamp')[0:2]
	paginator = Paginator(featured, 4)
	page = request.GET.get('page')
	featured = paginator.get_page(page)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render (request, 'blog.html' , {'object_list':featured,'latest':latest, 'last':last, 'posts': posts,
                'featured ' : featured , })

def blog_detail(request, id):

	Post = get_object_or_404(blog,id=id)
	last = blog.objects.order_by ('-timestamp')[0:2]
	return render (request, 'blog-single.html' ,{'Post' :Post , 'last':last } )




def shop(request):
	 data=Product.objects.all().order_by('-id')
	 cart = Cart(request)
	 if request.method == 'POST':
		 form = AddToCartForm(request.POST)
		 if form.is_valid():
			 quantity = form.cleaned_data['quantity']
			 prod_id= request.POST.get('prod_id')
			 cart.add(product_id=prod_id , quantity=quantity , update_quantity=True)
			 messages.success(request , 'Produit ajouter au Panier')
			 return HttpResponseRedirect(request.path_info)
	 
	 else:
		 form = AddToCartForm()


	 paginator = Paginator(data,9)
	 page = request.GET.get('page')
	 featured = paginator.get_page(page)
	 try:
		 posts = paginator.page(page)
	 except PageNotAnInteger:
		 posts = paginator.page(1)
	 except EmptyPage:
		 posts = paginator.page(paginator.num_pages)

	 return render(request, 'shop.html', {'data': data,  'posts': posts,'featured ': featured})


def cart_detail(request):
	cart = Cart(request)

	if request.method == 'POST':
		form = CheckoutForm(request.POST)

		if form.is_valid():
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				email = form.cleaned_data['email']
				country = form.cleaned_data['country']
				phone = form.cleaned_data['phone']
				address = form.cleaned_data['address']
				city = form.cleaned_data['city']
				zipcode = form.cleaned_data['zipcode']
								

				order = checkout(request,  first_name, last_name, email,country, address,city, zipcode, phone,
								 cart.get_total_cost() ,cart.get_total_cost_d())
			
				notify_customer(order)
				cart.clear()


				return redirect('success')
	else:
		form = CheckoutForm()

	remove_from_cart = request.GET.get('remove_from_cart', '')
	change_quantity = request.GET.get('change_quantity', '')
	quantity = request.GET.get('quantity', 0)

	if remove_from_cart:
		cart.remove(remove_from_cart)

		return redirect('cart')

	if change_quantity:
		cart.add(change_quantity, quantity, True)

		return redirect('cart')

	return render(request, 'cart.html', {'form': form,})

def success(request):
    return render(request, 'success.html')


def about(request):
    test = testimonial.objects.all()	
    return render(request, 'about.html', {'test':test})

def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        subject=request.POST.get('subject')
        contact.message=message
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        messages.success(request , 'Nous vous contacterons très bientot!')
        return HttpResponseRedirect(request.path_info)
    else:	
    	return render(request, 'contact.html')


def search(request):
	q=request.GET['q']
	featured=blog.objects.filter(title__icontains=q).order_by('-id')
	last = blog.objects.order_by('-timestamp')[0:2]
	paginator = Paginator(featured, 4)
	page = request.GET.get('page')
	featured = paginator.get_page(page)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request,'search.html',{'object_list':featured,'last':last ,'posts': posts,})



