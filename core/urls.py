from django.urls import path
from .views import (
   HomeView,
   ItemDetailView,
   add_to_cart,
   checkout) 


app_name= 'core'
urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   #path('',home,name='home'),
   path('product/<slug>/',ItemDetailView.as_view(),name='product'),
   path('checkout/',checkout,name='checkout'),
   path('add-to-cart/<slug>/',add_to_cart,name='add-to-cart'),
   
]