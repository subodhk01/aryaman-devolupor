from django.contrib import admin
from rooms.models import Room,Customer
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'room', 'checkedin','checkout','bill')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('roomid','status')