from django.urls import path
from products.views import *


app_name = 'products'

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),

    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page_number>/', ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),

    path('wishlists/add/<int:product_id>/', wishlist_add, name='wishlist_add'),
    path('wishlist/remove/<int:wishlist_id>/', wishlist_remove, name='wishlist_remove'),

    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('cart/', CartView.as_view(), name='cart'),

    path('about/', AboutUs.as_view(), name='about'),
    path('contacts/', Contacts.as_view(), name='contacts'),

]