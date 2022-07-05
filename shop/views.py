from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

#decorator and permission
from customuser.decorators import group_required
from customuser.mixins import CheckPremiumGroupMixin
from django.views.generic.list import ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from shop.admin import ArticleForm
from django.core import serializers

from .form import OrderForm
from .models import Article, ArticleUser, Cart, Product
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
# @group_required('namegroup')
# def group(request):
#     """for valid is in group .this not good. decorateur is good"""
#     if request.user.proups.filter(name='namegroup').exist():
#         return render(request, 'page.html')
#     else:
#         return HttpResponse('not in group')

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


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    article, created = ArticleUser.objects.get_or_create(user=user, product=product)
    
    if created:
        cart.articles.add(article)
        cart.save()
    else:
        article.quantity +=1
        article.save()
    return redirect('shop:index')


def checkout(request):
    user = request.user
    print(user)
    cart = get_object_or_404(Cart, user=user)
    cart_list = cart.articles.all()
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            form = OrderForm()
    return render(request, 'checkout.html', {'form': form, 'cart_list':cart_list})




def templates(request):
    return render(request, 'templates.html')

def temdetail(request):
    return render(request, 'detail_temp.html')



def indexajax(request):
    form = ArticleForm()
    articles = Article.objects.all()
    return render(request, 'indexajax.html', {'form': form, 'articles': articles})

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'



def add_article(request):
    # verifi ajax
    if is_ajax(request=request) and request.method == "POST":
        form = ArticleForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
    
    return JsonResponse({"error": ""}, status=400)        

