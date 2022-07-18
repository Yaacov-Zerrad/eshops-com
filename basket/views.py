from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict
from basket.models import Basket
from shop.models import Product

def basket_page(request):
    basket = Basket(request)
    # good -----request.session['basket']

    print('basket page')
    return render(request, 'basket/checkout.html', {'basket': basket})


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
        basket = 1# basket.__iter__()
        baskettotal = 1 # basket.get_total_price()
        return  JsonResponse({'qty': basketqty, 'subtotal': baskettotal} )


def basket_delete(request):
    basket = Basket(request)
    print('basket delete')
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = '1' # basket.get_total_price()
        response = JsonResponse({'qty': basketqty})
        return response


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
