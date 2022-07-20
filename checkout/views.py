import json
from turtle import update
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
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
        before_price = cart.total
        
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
                'before_price':before_price,
                'delivery_price': delivery_price,
                'total': update_total_price
            }
        else:
            session['price']['total'] = update_total_price
            session['price']['delivery_price'] = delivery_price
            session['price']['before_price'] = before_price
            session.modified =True
        
        response = JsonResponse({'total': update_total_price, 'delivery_price': delivery_price })
        return response
    
    
@login_required
def delivery_address(request):
    session = request.session
    price = session['price']
    
    if 'delivery' not in session:
        messages.success(request, 'Please select delivery options')
        # meta ... capture de l url (on peut faire ca pour revenir ou faire des condition ca depant d ou on vien)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    addresses = Address.objects.filter(user=request.user).order_by('-default')
    if addresses:
        if 'address' not in request.session:
                session['address'] = {
                    'address_id': str(addresses[0].id)
                }
        else:
            session['address']['address_id'] = str(addresses[0].id)
            session.modified =True
    
        return render(request, 'checkout/delivery_address.html', {'price':price, 'addresses':addresses})
    return render(request, 'checkout/delivery_address.html', {'price':price, 'addresses':addresses})


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


# from paypalcheckoutsdk.orders import OrdersGetRequest

# from .paypal import PayPalClient
# # on peut tou faire en recuperent leur inform depui leur log capture

body = ''
@login_required
def payment_complete(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user = request.user
        user_id = request.user.id

        purchase_units = body['purchase_units'][0]


        total_price =purchase_units['amount']['value']
        total_price = float(total_price)
        name =purchase_units['shipping']['name']['full_name']
        address =purchase_units['shipping']['address']['address_line_1']
        email = body[ 'payer']['email_address']
        city =purchase_units['shipping']['address']['country_code']
        country =purchase_units['shipping']['address']['country_code']
        zipcode =purchase_units['shipping']['address']['postal_code']
        num_order = body['id']

        print( total_price, name, city, zipcode, address, email, num_order)

        
        cart = Cart.objects.get(user=request.user)
        print(cart)
        order = Order.objects.create(
            user = user,
            name =purchase_units['shipping']['name']['full_name'],
            address =purchase_units['shipping']['address']['address_line_1'],
            email = body[ 'payer']['email_address'],
            city =purchase_units['shipping']['address']['country_code'],
            country =purchase_units['shipping']['address']['country_code'],
            zipcode =purchase_units['shipping']['address']['postal_code'],
            total_price =purchase_units['amount']['value'],
            qte = cart.qte,
        #     # achanger au payement
            activate =  True,
            num_order = body['id'],
            )
        # cart.delete()
        order.items.add(cart)
        order.save()
        

        return JsonResponse({'data':'success'})
        # return redirect('payment_successful')
    
    messages.success(request, 'Paypal payment not found')
        # meta ... capture de l url (on peut faire ca pour revenir ou faire des condition ca depant d ou on vien)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    


@login_required
def payment_successful(request):
    cart = Cart.objects.filter(user=request.user)
    # cart.delete()
    return render(request, "checkout/payment_successful.html", {})


