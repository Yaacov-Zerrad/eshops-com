# this metod is not modal is inclued a basquet in session
# a good is 2 basque 1 in cookies and one in session
from decimal import Decimal
from checkout.models import DeliveryOptions
from eshops import settings
from shop.models import Product

class Basket:
    # a base basket class can herit and overrided
    def __init__(self, request):
        """
        create basquet in request.session
        """
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in request.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket
            
            
    def add(self, product):
        """
        add product in basket (updating the basket in session data
        """
        product_id = str(product.id)
        
        if product_id in self.basket:
            self.basket[product_id]['qty'] +=1
        else:
            self.basket[product_id] = {'name':product.title ,'price': str(product.price), 'qty':1}

        self.save()
        
        
    def dimin(self, product):
        """
        add product in basket (updating the basket in session data
        """
        product_id = str(product.id)
        
        if product_id in self.basket:
            if self.basket[product_id]['qty'] > 1:
                self.basket[product_id]['qty'] -=1
            else:
                self.delete(product=product_id)
        # else:
        #     self.basket[product_id] = {'price': str(product.price), 'qty':1}

        self.save()




    def get_total_price(self):
        newprice = 0.00
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

        total = subtotal + Decimal(newprice)
        return total

 
    
    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]["product"] = product

        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item
    
        
    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item["qty"] for item in self.basket.values())
        
        
        
        
    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def clear(self):
        # Remove basket from session
        del self.session[settings.BASKET_SESSION_ID]
        del self.session["address"]
        del self.session["purchase"]
        self.save()

    def save(self):
        self.session.modified = True