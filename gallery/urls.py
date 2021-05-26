from django.http.request import QueryDict
from django.urls import path
from .views import CreateProduct, ProductDetails, ProductList
app_name = 'gallery'
urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('posts/<user>/', ProductList.as_view(), name='listself'),
    path('product/<pk>/', ProductDetails.as_view(), name='details'),
    path('create/', CreateProduct.as_view(), name='create'),
]
