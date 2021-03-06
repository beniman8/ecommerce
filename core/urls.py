from django.urls import path
from .views import (
   HomeView,
   ItemDetailView,
   remove_single_item_from_cart,
   add_to_cart,
   OrderSummaryView,
   remove_from_cart,
   CheckoutView,
   PaymentView,
   AddCouponView,
   RequestRefundView

  ) 


app_name= 'core'
urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   #path('',home,name='home'),
   path('order-summary/',OrderSummaryView.as_view(),name='order-summary'),
   path('product/<slug>/',ItemDetailView.as_view(),name='product'),
   path('checkout/',CheckoutView.as_view(),name='checkout'),
   path('add-to-cart/<slug>/',add_to_cart,name='add-to-cart'),
   path('add-coupon/',AddCouponView.as_view(),name='add-coupon'),
   path('remove_from_cart/<slug>/',remove_from_cart,name='remove_from_cart'),
   path('remove_single_item_from_cart/<slug>/',remove_single_item_from_cart,name='remove_single_item_from_cart'),
   path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
   path('request-refund/', RequestRefundView.as_view(), name='refund'),
   
]
