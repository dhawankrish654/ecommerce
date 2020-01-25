from django.shortcuts import render
from .forms import CustomerForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Category,Product,Order_Details,Orders,Customer,Cart
from django.db.models import Count

def index(request):
    #return HttpResponse("welcome to niit")
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'categories': categories, 'products': products})
def bycat(request,id):
    #return HttpResponse('welcome to niit')
    categories=Category.objects.all()
    products=Product.objects.filter(category_id=id)
    return render(request,'shop/index.html',{'categories':categories,'products':products})
    
@login_required(login_url='/login')
def addtocart(request,id):
    #return HttpResponse('welcome to niit')
    product=Product.objects.get(id=id)
    cust = Customer.objects.get(id=1)
    q=Cart(customer_id=cust,product_id=product,product_name=product.product_name,product_price=product.product_price)
    q.save()
    categories=Category.objects.all()
    products=Product.objects.all()
    return render(request,'shop/index.html',{'categories':categories,'products':products})
def viewcart(request,id):
    #return HttpResponse('welcome to niit')
    categories = Category.objects.all()
    mycart = Cart.objects.values('product_id','product_name','product_price').filter(customer_id=id).annotate(total=Count('product_id_id'))
    return render(request, 'shop/cartv.html', {'categories':categories,'mycart':mycart})
def deletecart(request,id):
    #return HttpResponse('welcome to niit')
    mycart=Cart.objects.filter(product_id=id)
    mycart.delete()
    categories = Category.objects.all()
    mycart = Cart.objects.values('product_id','product_name','product_price').filter(customer_id=1).annotate(total=Count('product_id_id'))
    return render(request, 'shop/cartv.html', {'categories':categories,'mycart':mycart})
def register(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
           form.save()
           userObj = form.cleaned_data
           username = userObj['cust_name']
           email = userObj['cust_email']
           password = userObj['cust_password']
           if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
             User.objects.create_user(username, email, password)
             user = authenticate(username=username, password=password)
             login(request, user)
             return HttpResponseRedirect('/')
           else:
             raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form=CustomerForm
    return render(request,'shop/register.html',{'form':form})

