from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

#decorator and permission
from customuser.decorators import group_required
from customuser.mixins import CheckPremiumGroupMixin
from django.views.generic.list import ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin


from .form import OrderForm
from .models import Product
from django.core.paginator import Paginator




def index(request):
    product_list = Product.objects.all()
    # search bar
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_list = Product.objects.filter(title__icontains=item_name)
    
    # paginate number product in page
    paginator = Paginator(product_list, 6) 
    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    
    return render(request, 'index.html', {'product_list': product_list})



#-----------------------------------------
# GROUP
#fabriquer dans account
@group_required('namegroup')
def group(request):
    """for valid is in group .this not good. decorateur is good"""
    if request.user.proups.filter(name='namegroup').exist():
        return render(request, 'page.html')
    else:
        return HttpResponse('not in group')

# group in class
#fabriquer dans account
class GroupPerm(CheckPremiumGroupMixin, ListView):
    # in path views.GroupPerm.as_view()
    model = Product
    template_name = 'page.html'
    
    
#for add in group
# if member in staff
@staff_member_required
def addToNameGroup(request):
    group = Group.objects.get(name='namegroup')
    request.user.groups.add(group)
    return HttpResponse('add in namegroup')

#-----------------------------------------
# PERMISSION

@permission_required('product.add_product')
def addProduct(request):
    return render(request, 'add.html')

# for class idem de group mais deja pret
class PermPerm(PermissionRequiredMixin, ListView):
    # in path views.GroupPerm.as_view()
    model = Product
    template_name = 'page.html'
    permission_required = ('product.add_product')
#-------------------------------------
    
# 2eme maniere
    # if request.user.has_perm('product.add_product'):# has_perms for multipl perms
    #     pass
    # else:
    #     pass
    
    
    
    
    
#---------------------------


def detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'detail.html', {'product': product })


def checkout(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            form = OrderForm()
    return render(request, 'checkout.html', {'form': form})




def templates(request):
    return render(request, 'templates.html')

def temdetail(request):
    return render(request, 'detail_temp.html')
