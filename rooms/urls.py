from django.urls import path
from rooms.views import *
urlpatterns=[
    path('', index, name="index"),
    path('customerslist/',customerslistview,name="customers_list"),
    path('newcustomer/',newCustomerview,name="new_customer"),
    path('customer/<int:cid>/', customerDetailview, name="customer-detail" ),
    path('rooms/',roomView,name="rooms_list"),
    path('room/<int:rid>/',roomCustomerView,name="room-customer"),
]