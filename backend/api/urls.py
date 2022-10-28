from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_user_portfolio,name='api-user-portfolio'), #shows routes
]