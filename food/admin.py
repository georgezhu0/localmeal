from django.contrib import admin
from food.models import College,Consumer,Swarthmore_Service,Haverford_Service,Transaction,Driver

# Register your models here.


admin.site.register(Swarthmore_Service)
admin.site.register(Haverford_Service)
admin.site.register(Consumer)
admin.site.register(Transaction)
admin.site.register(Driver)
