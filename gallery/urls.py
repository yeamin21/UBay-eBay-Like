from django.http.request import QueryDict
from django.urls import path
from .views import CreateProduct, ProductList
app_name = 'gallery'
urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<user>/', ProductList.as_view(), name='listself'),
    path('create/', CreateProduct.as_view(), name='create'),


]
