from django.urls import path
from myplog.views import helloworld,printname,myploghome,myproducts,productindex,index,show,delete,UpdateProductView, CreateProductView


urlpatterns = [
    path("hello",helloworld),
    #path("welcom/<name>",printname)
    path("home",myploghome),
    path('index',productindex),
    path('products',myproducts), 
    path("", index, name="myplog.index"),
    path("<int:id>", show, name= "myplog.show"),
    path("delete/<id>", delete, name ='myplog.delete'),
    path("edit/<int:pk>", UpdateProductView.as_view(), name="myplog.edit"),
    path("create", CreateProductView.as_view(), name="myplog.create")
    
]
