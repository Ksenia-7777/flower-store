from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
# Create your views here.
from products.models import Basket, Product, ProductCategory, Wishlist, FeaturedProducts

from django.core.paginator import Paginator

from django.shortcuts import render

# class IndexView(TitleMixin, TemplateView):
#     model = FeaturedProducts
#     template_name = 'products/index-3.html'
#     title = 'Store'

class IndexView(TitleMixin, ListView):
    model = FeaturedProducts
    template_name = 'products/index-3.html'
    title = 'Store'

class WishlistView(TitleMixin, TemplateView):
    template_name = 'products/wishlist.html'
    title = 'Wishlist'

class CartView(TitleMixin, TemplateView):
    template_name = 'products/cart.html'
    title = 'Cart'



class ProductsListView(TitleMixin, ListView):
    model = Product
    # template_name = 'products/products.html'
    template_name = 'products/shop.html'
    paginate_by = 9
    title = 'Store - Каталог'

    context_object_name = 'product'


    # def get_queryset(self):
    #     queryset = super(ProductsListView, self).get_queryset()
    #     category_id = self.kwargs.get('category_id')
    #     return queryset.filter(category_id=category_id) if category_id else queryset

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        name__icontains = self.request.GET.get('q')

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if name__icontains:
            queryset = queryset.filter(name__icontains=name__icontains)

        return queryset

#     < form
#     action = "#"
#     method = "get" >
#     < input
#     type = "search"
#     type = "text"
#     name = "q"
#     placeholder = "поиск" >
#     < button
#     type = "submit" > Найти < / button >
#
# < / form >

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['q'] = self.request.GET.get('q')
        return context



@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    #

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quntity=1)
    else:
        basket = baskets.first()
        basket.quntity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request,  basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def wishlist_add(request, product_id):
    print('1111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    product = Product.objects.get(id=product_id)
    wishlists = Wishlist.objects.filter(user=request.user, product=product)
    #

    if not wishlists.exists():
        print('///////////////////////////////////////////////////////////////////////////////////')
        Wishlist.objects.create(user=request.user, product=product, quntity=1)
    else:
        print('###############################################################################')
        wishlist = wishlists.first()
        wishlist.quntity += 1
        wishlist.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
