from django.db.models.signals import m2m_changed,  post_save, pre_save, pre_delete
from django.dispatch import receiver
from customuser.models import User
# from vente.models import Sales
from .models import Article, Cart, Order, Product
import uuid

# -----------apps and init------------------------

@receiver(post_save, sender=User)
def add_cart_user(sender, instance, created, *args, **kwargs):
    if created:
        instance.save()
        cart = Cart.objects.create(user=instance)
        cart.save()
        
        
        # sender 
@receiver(m2m_changed, sender=Cart.articles.field)
def calcul_total(sender, instance, action, *args, **kwargs):
    """calcul price and qte in cart"""
    qte = 0
    total_price = 0
    for art in instance.articles.all():
        qte +=1
        total_price += art.total
    instance.qte = qte
    instance.total = total_price
    instance.save()
    
    
@receiver(pre_save, sender=Article)
def calcul_total_article(sender, instance,    *args, **kwargs):
    """calcul price des articles en eux meme"""
    total_price = 0
    for price in range(0, instance.quantity):
        total_price += instance.product.price
    instance.total = total_price
    
    
@receiver(pre_save, sender=Cart)
def calcul_total(sender, instance,    *args, **kwargs):
    """calcul price and qte in cart"""  
    qte =0
    total_price = 0
    #cart, _ = Cart.objects.get_or_create(user=instance.user)
    if Cart.objects.filter(user=instance.user):
        total_price = 0
        qte = 0
        articles = instance.articles.all()
        for article in articles:
            qte +=1
            total_price += article.total
        instance.qte = qte
        instance.total = total_price
    
    

     
# @receiver(pre_save, sender=Cart)
# def calcul_total(sender, instance,    *args, **kwargs):
#     #cart, _ = Cart.objects.get_or_create(user=instance.user)
#     """calcul price and qte in cart"""
#     total_price = 0
#     qte = 0
#     articles = instance.articles.all()
#     for article in articles:
#         qte +=1
#         total_price = article.total
#     instance.qte = qte
#     instance.total = total_price
    

     


# @receiver(post_save, sender=Cart)
# def post_save_sale(sender, instance, created, **kwargs):
#     # get and creat _
#     obj, _ = Order.objects.get_or_create(order=instance)
#     obj.amount = instance.total_price
#     obj.save()
    
        
@receiver(m2m_changed, sender=Order)
def pre_delete_orders(sender, instance, action,   **kwarg):
    obj = instance.items
    obj.ordered = True
    obj.save()
    
           
    # #relation buyer voiture si choisi une voitur (le rendre actif)
    # obj = Buyers.objects.get(user=instance.buyer.user)
    # obj.actif = True
    # obj.save()
    
    
@receiver(m2m_changed, sender=Order)
def orders(sender, instance,   **kwarg):
    toto = 0
    qte = 0
    for item in instance.items.all():
        toto += item.total  
    instance.total_price = toto
    instance.qte = item.qte
    if instance.num_order == "":
        instance.num_order = str(uuid.uuid4()).replace('-','').upper()[:10]
        instance.save()

@receiver(post_save, sender=Order)
def clear_cart(sender, instance, created, *args, **kwargs):
    if created:
        instance.items.all().delete()
            


# @receiver(post_save, sender=Cart)
# def pre_total_cart(sender, instance,  **kwarg):
#     """total in cart"""
#     # qte = instance.articles.through
#     # total = 0
#     # for article in qte:
#     #     total += instance.articles.product.price
#     instance.total = 122

#     instance.save()  
    
# @receiver(post_save, sender=Orders)
# def post_save_sale(sender, instance, created, **kwargs):
#     # get and creat _
#     obj, _ = Sales.objects.get_or_create(order=instance)
#     obj.amount = instance.total_price
#     obj.save()