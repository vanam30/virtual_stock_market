from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_routes,name='get-routes'),
    path('user',views.get_user_portfolio,name='api-user-portfolio'), #shows routes
    path('order',views.add_new_order,name='new-order'),
    path('price',views.get_market_price,name='market-price'),
]