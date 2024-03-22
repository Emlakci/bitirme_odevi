from django.shortcuts import render, redirect
from mainApp.models import *

# Create your views here.

def homePage(request):

    product = Products.objects.filter(p_season_category__season_name = 'Yazlik')
    product_best_seller = Products.objects.filter(p_special_status__states = 'Cok Satan Urun')

    context ={
        'product' : product,
        'best_seller' : product_best_seller,
    }

    request.session['visited_home'] = True
    return render(request,'index.html', context)

def shoppingPage(request):

    product = Products.objects.all()

    context ={
        'product' : product,
    }
    return render(request,'shoppingPage.html', context)

def productDetailsPage(request, p_id):

    request_product = Products.objects.get(id=p_id)
    p_size = request_product.p_sizes.all()
    same_category_product = Products.objects.filter(p_category=request_product.p_category).exclude(id=p_id) # don not get  request_product again

    img_fields = ['p_img_1', 'p_img_2', 'p_img_3', 'p_img_4']
    img_src = []

    for img_field in img_fields:
        existence = getattr(request_product, img_field, None)
        if existence:
            print(f"{img_field} alanı dolu")
            print('line43', getattr(request_product, img_field))
            img_src.append(getattr(request_product, img_field))
        else:
            print(f"{img_field} alanı boş")
  
    
    context ={
        'product': request_product,
        'img_src' : img_src,
        'p_size' : p_size,
        'same_product' : same_category_product,
    }
    
    return render(request,'productDetails.html', context)

def aboutPage(request):
    context ={}
    return render(request,'aboutPage.html', context)

def contactPage(request):
    if request.method == 'POST':
        name = request.POST.get('f-name')
        surname = request.POST.get('l-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if name and surname and email and phone and message :
            post = Contact(name=name, surname=surname, email=email, phone=phone, message=message)
            post.save()

    context ={}
    return render(request,'contactPage.html', context)

def categoryPage(request):
    context ={}
    return render(request,'categoryPage.html', context)