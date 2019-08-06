from django.contrib import admin

from .models import Item, Order, OrderItem,Payment,Coupon,Refund,Address

def  make_refund_accepted(ModelAdmin, request,queryset):
    queryset.update(refunds_requested=False,refund_granted=True)
make_refund_accepted.short_description="Update orders to refund granted"

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refunds_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon'
                    ]

    list_display_links = ['user',
                          'shipping_address',
                          'billing_address',
                          'payment',
                          'coupon']

    search_fields = ['user__username',
                     'ref_code']

                        
    
    list_filter = ['ordered',
                    'being_delivered',
                    'received',
                    'refunds_requested',
                    'refund_granted']

    actions = [make_refund_accepted]


class AdressAdmin(admin.ModelAdmin):
    list_display =['user',
                   'street_address', 
                   'apartment_address' ,
                   'country', 
                   'zip' ,
                   'address_type' ,
                   'default'
                

    ]
    list_filter = ['address_type', 
                   'default',
                   'country' ,

                    ]

    search_fields = [ 'user',
                      'street_address', 
                      'apartment_address' ,
                      'country', 
                      'zip' ,
                      'address_type' ,
                      'default']

 
      
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address,AdressAdmin)
