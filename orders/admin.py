from django.contrib import admin
from .models import Order

# Register your models here.

class OrderInLine(admin.TabularInline):
    model = Order
    extra = 1 #number of extra blank forms 
    readonly_fields = ['total_price']
    can_delete=True 

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status','items', 'ordered_at', 'total_amount_display']
    list_filter = ['status', 'ordered_at']
    search_fields = ['customer__name']
    linlines = [OrderInLine]

    def total_amount_display(self, obj):
        return obj.total_price

