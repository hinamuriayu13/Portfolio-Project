from django.contrib import admin
from .models import UserProfile, Category, Product, Cart, Order

# Register the models that do not need customization
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)

# Custom admin class for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category', 'stock', 'image')
    readonly_fields = ('id',)  # Make the id field read-only in the admin form

# Register Product with the custom ProductAdmin class
admin.site.register(Product, ProductAdmin)
