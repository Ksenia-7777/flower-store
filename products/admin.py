# Register your models here.

# admin.site.register(Product)
# admin.site.register(ProductCategory)


from django.contrib import admin

from products.models import Basket, Product, ProductCategory, FeaturedProducts

admin.site.register(ProductCategory)
admin.site.register(FeaturedProducts)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quntity', 'category')
    fields = ('image', 'name', 'description', ('price', 'quntity'), 'stripe_product_price_id', 'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('-name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quntity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0