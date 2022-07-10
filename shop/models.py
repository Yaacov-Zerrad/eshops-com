from django.utils import timezone
from django.db import models

from eshops.settings import AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        """for premiere ligne selon date"""
        ordering = ['-date_added']
        
        
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    stock = models.IntegerField(default=0)
    #  etranger key
    Category =models.ForeignKey("Category",  on_delete=models.CASCADE, related_name='category')
    # for image upload 
    # img = models.ImageField
    img = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-date_added']
        
    def __str__(self):
        return self.title
    
# ---------create new permition in migrate

    # class Meta:
    #     permissions = (
    #         ('Can_name_permission1', 'description'),
    #         ('Can_name_permission2', 'description'),
    #     )
    
    
#--------------------------create new permission in terminal

# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType

# ct = ContentType.objects.get_for_model(Product)
# permission = Permission.objects.create(codename='can_do_this', contentype=ct)
    
# ----------------new permission for all model

# class CustomPermissions(models.model):

#     class meta:     
#         # for no database create
#         managed = False 
#         #for not create default permissions
#         default_permissions = () 
#     # new permission

        # permissions = (
        #     ('accept_order', 'can accept order'),
        #     ('reject_order', 'can reject order'),
        # )
        
class Article(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(null=True, blank=True)
    
    
    def __str__(self):
        return self.product.title

        



class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article)
    total = models.FloatField(blank=True, null=True)
    qte = models.PositiveIntegerField(blank=True, null=True)
    # class Meta:
    #     ordering = ['-ordered_date']
        
    def __str__(self):
        return self.user.email
    
    def delete(self, *args, **kwargs):
        """save article ordered and clear cart"""
        for article in self.articles.all():
            print(article)
            article.ordered =True
            article.ordered_date = timezone.now()
            article.save()
        self.articles.clear()   
        super().delete(*args, **kwargs)
    
    
    
class Order(models.Model):
    # items = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=127)
    address = models.CharField(max_length=127)
    city = models.CharField(max_length=127)
    country = models.CharField(max_length=127)
    zipcode = models.CharField(max_length=127)
    date_added = models.DateTimeField(auto_now=True)
    
    items = models.ManyToManyField(Cart)
    qte = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    activate = models.BooleanField(default=True)
    num_order = models.CharField(max_length=50, blank=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date_added']
    