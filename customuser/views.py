import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from customuser.forms import AddressForm
from customuser.models import Address
from django.core import serializers

# address view
@login_required
def address_view(request):
    return render(request, 'customuser/address_view.html')


#adrress content
@login_required
def address_list(request):
    addresses = Address.objects.filter(user=request.user)
    
    addresses = serializers.serialize('json', addresses)
    data=  {'addresses': json.loads(addresses)}
    return JsonResponse(data)


#address form (add)
@login_required
def address_form(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddressForm()
            return redirect('customuser:address_view')
    return render(request, 'customuser/address_form.html', {'form':form})





#address update
@login_required
def address_update(request, pk):
    previous_url = request.META.get("HTTP_REFERER")
    ar = str(previous_url)
    address = get_object_or_404(Address, id=pk)
    form = AddressForm(instance=address)
    print('url1 :', ar) 
    if request.method == 'POST':
        if form.is_valid:
            print('url 2:', ar) 
            form = AddressForm(data=request.POST, instance=address)
            form.save()
            return redirect("customuser:address_view")
    return render(request, 'customuser/address_form.html', {'form': form})

#address default
@login_required
def address_default(request, pk):
    Address.objects.filter(user=request.user, default=True).update(default=False)
    Address.objects.filter(id=pk, user=request.user).update(default=True)

    previous_url = request.META.get("HTTP_REFERER")

    if "delivery_address" in previous_url:
        return redirect("check:delivery_address")
    return redirect("customuser:address_view")



#address delete
@login_required
def address_delete(request, pk):
    obj = get_object_or_404(Address, id=pk)
    name = obj.name
    if request.method == 'POST':
        obj.delete()
        return redirect('customuser:address_view')
    return render(request, 'customuser/address_delete.html', {'name': name})










