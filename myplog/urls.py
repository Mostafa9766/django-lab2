from django.urls import path
from myplog.views import helloworld,printname,myploghome,myproducts,productindex


urlpatterns = [
    path("hello",helloworld),
    #path("welcom/<name>",printname)
    path("home",myploghome),
    path('index',productindex),
    path('products',myproducts), 
    
]
