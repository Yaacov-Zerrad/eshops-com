import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict
from basket.models import Basket
# from basket.serializers import BasketSerializer
from shop.models import Product
from django.core import serializers




def basket_json(request):
    """json basket"""
    basket = Basket(request)
    data = request.session.get('basket')
    return JsonResponse(data)

def basket_view(request):
    return render(request, 'basket/basket_view.html')




def basket_page(request):
    basket = Basket(request)
    # good -----request.session['basket']

    print('basket page')

    return render(request, 'basket/checkout.html', {'basket': basket, })


def basket_add(request):
    basket = Basket(request)
    print('basket add')
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = Product.objects.get(id=product_id)
        basket.add(product=product)
        basket.save()
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        basket = request.session['basket']
        return  JsonResponse({'basket': basket, 'qty':basketqty, 'total':baskettotal} )


def basket_dimin(request):
    basket = Basket(request)
    print('basket dimin')
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = Product.objects.get(id=product_id)
        basket.dimin(product=product)
        basket.save()
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        basket = request.session['basket']
        return  JsonResponse({'basket': basket, 'qty':basketqty, 'total':baskettotal} )
    
    
def basket_delete(request):
    basket = Basket(request)
    print('basket dimin')
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        basket.save()
        basket = request.session['basket']
        return  JsonResponse({'basket': basket} )


# def basket_delete(request):
#     basket = Basket(request)
#     if request.method == 'POST':
#         print('basket delete')
#         # product_id = int(request.POST.get('productid'))
#         # basket.delete(product=product_id)

#     return  JsonResponse({'basket': 'basket'})


# def basket_update(request):
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         product_qty = int(request.POST.get('productqty'))
#         basket.update(product=product_id, qty=product_qty)

#         basketqty = basket.__len__()
#         basketsubtotal = basket.get_subtotal_price()
#         response = JsonResponse({'qty': basketqty, 'subtotal': basketsubtotal})
#         return response
