from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

# from vente.models import Sales
from .models import Order



@receiver(m2m_changed, sender=Order.items.through)
def m2m_changed_calculate(sender, instance, action, **kwargs):
    qte = 0
    total_price = 0
    for car in instance.cars.all():
        qte +=1
        total_price += car.price
    instance.qte = qte
    instance.total_price = total_price
    instance.save()
    
    
    
# @receiver(post_save, sender=Orders)
# def post_save_sale(sender, instance, created, **kwargs):
#     # get and creat _
#     obj, _ = Sales.objects.get_or_create(order=instance)
#     obj.amount = instance.total_price
#     obj.save()