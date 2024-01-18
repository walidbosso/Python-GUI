from django.shortcuts import render,redirect
from .models import Product
#from django.contrib import messages
# Create your views here.
def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})


def add(request):
    if request.method=="POST":
        name=request.POST['name']
        company=request.POST['company']
        price=request.POST['price']
        number_in_stock=request.POST['number_in_stock']
        Product.objects.create(name=name,company=company,price=price,number_in_stock=number_in_stock)
 #       messages.success(request,'Product has been registered')
    return render(request,'add.html')

def update(request,id):

    if request.method=="POST":
        name=request.POST['name']
        company=request.POST['company']
        price=request.POST['price']
        number_in_stock=request.POST['number_in_stock']
        Product.objects.filter(id=id).update(name=name,company=company,price=price,number_in_stock=number_in_stock)

    product=Product.objects.get(id=id)
    return render(request,'update.html',{'product':product})

def delete(request,id):
    Product.objects.filter(id=id).delete()
    return redirect('/')
