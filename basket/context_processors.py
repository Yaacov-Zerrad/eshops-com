from .models import Basket

def cart(request):
    return {'basket':Basket}