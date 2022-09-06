from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloworld(request):
    return HttpResponse("Hello World")
def printname(request,name):
    return HttpResponse(f"<h> welcome ya {name} ^-^<h>")
def myploghome(request):
    return render(request,'myplog/home.html')

def productindex(request):
    return HttpResponse("<h>This my products index page. <h>")

def myproducts(request):
    products=[ 

            {"id":1,"name":"Mobiles","image":"product1.png"},
            {"id":2,"name":"Playstations","image":"product2.png"},
            {"id":3,"name":"labtops","image":"product3.png"}
    ]
    content={"products":products}
    return render (request,'myplog/products.html',content)
