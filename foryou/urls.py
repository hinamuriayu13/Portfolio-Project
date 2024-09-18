from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This routes the root URL to the index view
    path('product/<int:id>/', views.product_page, name='product_page'),

     # Login and register views
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register_view'),
    
    # Logout and profile
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),

    #cart urls
    path('cart/', views.cart_summary,name="cart_summary"),
    path('add/', views.cart_add , name="cart_add"),
    path('delete/', views.cart_delete , name="cart_delete"),
    path('update/', views.cart_update , name="cart_update"),
]
