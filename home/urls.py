from django.urls import path
from . import views


urlpatterns = [

    path('', views.home , name='home') ,
    path('products', views.products_views , name='products_views') ,
    path('detail/<str:pk>', views.detail_view , name='detail_view') ,
    path('about', views.about_us_views , name='about_us_views') ,
    path('cart/<str:pk>', views.add_cart_view , name='add_cart_view') ,
    path('cart', views.cart_view , name='cart_view') ,

]
