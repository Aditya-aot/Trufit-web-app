from django.shortcuts import render
from django.shortcuts import render ,redirect
# Create your views here.

from .models import category_model , product_model ,cart_model ,basic_image




def home(request) :
    image = basic_image.objects.all()
    logo_images =  image.filter(name="trufit")
    cart_images =  image.filter(name="cart")


    context={
        'logo_image' : logo_images ,
        'cart_images' : cart_images ,


    }
    return render(request , 'home/home.html' , context)


def products_views(request) :
    image = basic_image.objects.all()
    logo_images =  image.filter(name="trufit")
    cart_images =  image.filter(name="cart")

    product = product_model.objects.all()

    context = {
        'product' : product[::-1] ,
        'logo_image' : logo_images ,
        'cart_images' : cart_images ,
    }
    return render(request , 'home/products.html', context)


def detail_view(request,pk) :
    image = basic_image.objects.all()
    logo_images =  image.filter(name="trufit")
    cart_images =  image.filter(name="cart")

    product = product_model.objects.all()
    product_info = product.filter(id=pk)
    price = product_info.values("price") 
    print(price[0])



    context = {
            'product' : product_info ,
            'top_product' : product[::-1] ,

            'logo_image' : logo_images ,
            'cart_images' : cart_images ,
        }
    return render(request, 'home/detail.html',context)









def about_us_views(request) :
    image = basic_image.objects.all()
    logo_images =  image.filter(name="trufit")
    cart_images =  image.filter(name="cart")

    context = {'logo_image' : logo_images ,
        'cart_images' : cart_images ,

    }
    return render(request , 'home/about.html', context)


def add_cart_view(request, pk) :
    qty = int(request.GET["qty"])
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',qty,pk)
    user_cart = cart_model(user=request.user, product_id=pk,quantity=qty)
    user_cart.save()

    return redirect("/cart")
    # return render(request , 'home/cart.html')



def cart_view(request ) :
    image = basic_image.objects.all()
    logo_images =  image.filter(name="trufit")
    cart_images =  image.filter(name="cart")


    cart = cart_model.objects.all()
    cart_user = cart.filter(user=request.user)


    context = {'logo_image' : logo_images ,
        'cart_images' : cart_images ,
        'cart' : cart_user[::-1]
    }
    return render(request , 'home/cart.html', context)
