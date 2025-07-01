from django.contrib import admin
from .models import

class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False

# --- DO'KON 1 ---

@admin.register(CategoryStore1)
class CategoryStore1Admin(ReadOnlyAdmin):
    list_display = ('id', 'name', 'created_at')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store1')

@admin.register(ProductStore1)
class ProductStore1Admin(ReadOnlyAdmin):
    list_display = ('id', 'name', 'barcode', 'category', 'unit', 'created_at')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store1')

@admin.register(ProductBatchStore1)
class ProductBatchStore1Admin(ReadOnlyAdmin):
    list_display = ('id', 'product', 'batch_number', 'purchase_price', 'selling_price', 'initial_quantity', 'remaining_quantity', 'arrival_date', 'expiry_date')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store1')

@admin.register(SaleStore1)
class SaleStore1Admin(ReadOnlyAdmin):
    list_display = ('id', 'sale_number', 'cashier', 'total_amount', 'payment_method', 'status', 'created_at')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store1')

@admin.register(SaleItemStore1)
class SaleItemStore1Admin(ReadOnlyAdmin):
    list_display = ('id', 'sale', 'product', 'batch', 'quantity', 'unit_price', 'total_price', 'returned_quantity')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store1')

@admin.register(ReturnSaleStore1)
class ReturnSaleStore1Admin(ReadOnlyAdmin):
    list_display = ('id', 'original_sale', 'return_number', 'cashier', 'total_return_amount', 'created_at')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store1')

@admin.register(ReturnItemStore1)
class ReturnItemStore1Admin(ReadOnlyAdmin):
    list_display = ('id', 'return_sale', 'sale_item', 'returned_quantity', 'return_amount')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store1')

# --- DO'KON 2 ---

@admin.register(CategoryStore2)
class CategoryStore2Admin(ReadOnlyAdmin):
    list_display = ('id', 'name', 'created_at')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store2')

@admin.register(ProductStore2)
class ProductStore2Admin(ReadOnlyAdmin):
    list_display = ('id', 'name', 'barcode', 'category', 'unit', 'created_at')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store2')

@admin.register(ProductBatchStore2)
class ProductBatchStore2Admin(ReadOnlyAdmin):
    list_display = ('id', 'product', 'batch_number', 'purchase_price', 'selling_price', 'initial_quantity', 'remaining_quantity', 'arrival_date', 'expiry_date')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store2')

@admin.register(SaleStore2)
class SaleStore2Admin(ReadOnlyAdmin):
    list_display = ('id', 'sale_number', 'cashier', 'total_amount', 'payment_method', 'status', 'created_at')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store2')

@admin.register(SaleItemStore2)
class SaleItemStore2Admin(ReadOnlyAdmin):
    list_display = ('id', 'sale', 'product', 'batch', 'quantity', 'unit_price', 'total_price', 'returned_quantity')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store2')

@admin.register(ReturnSaleStore2)
class ReturnSaleStore2Admin(ReadOnlyAdmin):
    list_display = ('id', 'original_sale', 'return_number', 'cashier', 'total_return_amount', 'created_at')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store2')

@admin.register(ReturnItemStore2)
class ReturnItemStore2Admin(ReadOnlyAdmin):
    list_display = ('id', 'return_sale', 'sale_item', 'returned_quantity', 'return_amount')
    def get_queryset(self, request):
        return super().get_queryset(request).using('store2')

# --- ADMIN PANEL Sarlavhasi ---
admin.site.site_header = "Barcha Do'konlar Ma'lumotlari"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Do'konlarni boshqarish"