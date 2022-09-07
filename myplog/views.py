from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myplog.models import  Product
from myplog.forms import ProductForm
from django.views.generic.edit import UpdateView, CreateView

# Create your views here.
def helloworld(request):
    return HttpResponse("Hello World")
def printname(request,name):
    return HttpResponse(f"<h> welcome ya {name} ^-^<h>")
def myploghome(request):
    return render(request,'myplog/home.html')

def productindex(request):
    return HttpResponse("<h>This is my products index page. <h>")

def myproducts(request):
    products=[ 

            {"id":1,"name":"Mobiles","image":"product1.png"},
            {"id":2,"name":"Playstations","image":"product2.png"},
            {"id":3,"name":"labtops","image":"product3.png"}
    ]
    content={"products":products}
    return render (request,'myplog/products.html',content)
def index(request):
    products = Product.objects.all()
    return  render(request, "myplog/index.html", context={"products":products})


def index(request):
    products = Product.objects.all()
    return  render(request, "myplog/index.html", context={"products":products})



def show(request, id):
    product = Product.objects.get(pk=id)
    # return HttpResponse(product)
    print(product.get_show_url())
    return  render(request, "myplog/show.html", context={"product":product})



def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect("/myplog")


class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name ='myplog/edit.html'
    success_url = "/myplog"



class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name ='myplog/create.html'
    success_url = "/myplog"
