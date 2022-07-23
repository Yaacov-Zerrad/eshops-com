from django.forms import JSONField
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

#decorator and permission
from customuser.decorators import group_required
from customuser.mixins import CheckPremiumGroupMixin
from django.views.generic.list import ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from shop.admin import ArticleForm
from django.core import serializers

from .form import OrderForm
from .models import Article, Cart, Category, Product
from django.core.paginator import Paginator




def index(request):
    """product list"""
    product_list = Product.objects.all()
    # search bar
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_list = Product.objects.filter(title__icontains=item_name)
    
    # paginate number product in page
    paginator = Paginator(product_list, 8) 
    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    
    return render(request, 'index.html', {'product_list': product_list})


def detail(request, pk):
    """detail product"""
    form = ArticleForm()
    articles = Article.objects.all()
    product = get_object_or_404(Product, id=pk)
    return render(request, 'detail.html', {'product': product, 'form': form, 'articles': articles })

#----------- not useful
@login_required
def checkout(request):
    """cart and achat"""
    user = request.user
    print(user)
    cart, _ = Cart.objects.get_or_create(user=user)
    cart_list = cart.articles.all()
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            form = OrderForm()
    return render(request, 'checkout.html', {'form': form, 'cart_list':cart_list})



#----------- not useful
@login_required
def add_article(request):
    """add article in db en ajax """
    if request.method == "POST":
        slug = request.POST["slug"]
        print(slug)
        user = request.user
        product = get_object_or_404(Product, slug=slug)
        cart, _ = Cart.objects.get_or_create(user=user)
        article, created = Article.objects.get_or_create(user=user, ordered=False, product=product)
        
        if created:
            cart.articles.add(article)
            instance = cart.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ article.product, ])
            print(article)
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        
        if not created:
            article.quantity +=1
            instance = article.save()
            
            # serialize in new friend object in json
            print(article.product.description)
            ser_instance = serializers.serialize('json', [ article.product, ])
            print(ser_instance)
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": "form.errors"}, status=400)
    
    return JsonResponse({"error": ""}, status=400) 

#----------- not useful
@login_required
def get_data_cart(request):
    """get table cart in json"""
    articles = Article.objects.filter(ordered=False, user=request.user)
    dictionary =  list([{'product':article.product.title, 'quantity':article.quantity}  for article in articles]  )
    return JsonResponse({'articles':dictionary})

#----------- not useful
@login_required
def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()
    return redirect('index')


#----------- not useful
@login_required
def add_product_test(request):
    """add product sans ce casser la tete"""
    bck= Category.objects.get(name='bck')
    print(bck)
    for i in range(1, 23):
        product = Product.objects.create(title=f'product_{i}', price=32, description="super article", slug=f'slug{i}', Category=bck, stock=i, img='https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg?auto=compress&cs=tinysrgb&w=300')
    return JsonResponse(product.objects.all())






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
    
    
    