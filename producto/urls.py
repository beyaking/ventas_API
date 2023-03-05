from django.urls import path, include
from producto import views
urlpatterns = [
    path('listProduct', views.ProductList.as_view() ),
    path('createProduct', views.ProductCreate.as_view() ),
    path('productDetail/<int:pk>', views.ProductDetail.as_view() ),
    path('productView', views.ProductView.as_view() )
    
]