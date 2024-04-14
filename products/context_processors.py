from products.models import Basket, Wishlist


def baskets(request):
    user = request.user
    return {'baskets': Basket.objects.filter(user=user) if user.is_authenticated else [],
            'wishlists': Wishlist.objects.filter(user=user) if user.is_authenticated else []}

