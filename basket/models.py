# this metod is not modal is inclued a basquet in session
# a good is 2 basque 1 in cookies and one in session
from eshops import settings

class Basket:
    # a base basket class can herit and overrided
    def __init__(self, request):
        """
        create basquet in request.session
        """
        self.session = request.session
        # implante in setting
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
            self.basket[product_id] = {'price': str(product.price), 'qty':1}

        self.save()
        
        
        
        
        
        
        
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