import json
from turtle import update
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from customuser.models import Address

from shop.models import Cart, Order

from .models import DeliveryOptions

@login_required
def deliverychoices(request):
    """choix ou delivery"""
    deliveryoptions = DeliveryOptions.objects.filter(is_active=True)
    cart = Cart.objects.filter(user=request.user)
    cart = cart[0]
    return render(request, 'checkout/delivery_choices.html', {'deliveryoptions':deliveryoptions, 'cart':cart})



@login_required
def cart_update_delivery(request):
    cart = Cart.objects.filter(user=request.user)
    cart = cart[0]
    print(cart.total)
    # for verifi post and ajax
    if request.POST.get('action') == 'post':
        # for recup id for integre in the session
        delivery_option = int(request.POST.get('deliveryoption'))
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
        # for calcul if delivery is payant
        # update_total_price = cart.cart_update_delivery(delivery_type.delivery_price)
        
        delivery_price = int(delivery_type.delivery_price)
        update_total_price = cart.total +int( delivery_price)
        
        #add in session
        session = request.session
        if 'delivery' not in request.session:
            session['delivery'] = {
                'delivery_id': delivery_type.id,
            }
        else:
            session['delivery']['delivery_id'] = delivery_type.id
            session.modified =True
            
        if 'price' not in request.session:
            session['price'] = {
                'total': update_total_price,
                'delivery_price': delivery_price
            }
        else:
            session['price']['total'] = update_total_price
            session['price']['delivery_price'] = delivery_price
            session.modified =True
        
        response = JsonResponse({'total': update_total_price, 'delivery_price': delivery_price })
        return response
    
    
@login_required
def delivery_address(request):
    session = request.session
    cart = Cart.objects.get(user=request.user)
    if 'delivery' not in session:
        messages.success(request, 'Please select delivery options')
        # meta ... capture de l url (on peut faire ca pour revenir ou faire des condition ca depant d ou on vien)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    addresses = Address.objects.filter(user=request.user).order_by('-default')
    
    if 'address' not in request.session:
            session['address'] = {
                'address_id': str(addresses[0].id)
            }
    else:
        session['address']['address_id'] = str(addresses[0].id)
        session.modified =True
    
    return render(request, 'checkout/delivery_address.html', {'addresses':addresses, 'total':cart.total})


@login_required
def payment_selection(request):
    session = request.session
    price = session['price']
    print(session['delivery'])
    if 'address' not in request.session:
        messages.success(request, 'Please select address option')
        # meta ... capture de l url (on peut faire ca pour revenir ou faire des condition ca depant d ou on vien)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
    return render(request, 'checkout/payment_selection.html', {'price':price})


from paypalcheckoutsdk.orders import OrdersGetRequest

from .paypal import PayPalClient
# on peut tou faire en recuperent leur inform depui leur log capture


@login_required
def payment_complete(request):
    PPClient = PayPalClient()
    print('asd', PPClient)
    body = json.loads(request.body)
    data = body['orderID']
    user_id = request.user.id
    requestorder =  OrdersGetRequest(data)
    response = PPClient.client.execute(requestorder)
    
    # total_paid = response.result.purchase_units[0].amount.value
    
    # cart = Cart.objects.get(user=request.user, ordered=False,)
    # order = Order.objects.create(
    #     name =  response.result.purchase_units[0].shipping.name.full_name,
    #     email = response.result.payer.email_address,
    #     address = response.result.purchase_units[0].shipping.address.address_line_1,
    #     city = response.result.purchase_units[0].shipping.address.country_code,
    #     country = response.result.purchase_units[0].shipping.address.country_code,
    #     zipcode = response.result.purchase_units[0].shipping.address.postal_code,
    #     items = cart,
    #     qte = cart.qte,
    #     total_price = total_paid,
    #     # achanger au payement
    #     activate =  True,
    #     num_order = response.result.id,
    # )
    # cart.delete()
    
    return JsonResponse('Payment completed', safe=False)


@login_required
def payment_successful(request):
    return HttpResponse('marche')


