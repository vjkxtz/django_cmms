from django.contrib import admin
from .models import Carrier, LineHistory, Carrier_number, Stop_numbers, Stop, Tsw_number, Tsw 

# Register your models here.

@admin.register(LineHistory)
class LineHistoryAdmin(admin.ModelAdmin):
    list_display = ('line', 'assembly')


@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ('carrier_num'  , 'work_done' )


@admin.register(Carrier_number)
class Carrier_numberAdmin(admin.ModelAdmin):
    list_display = ('carrier_num', 'greasing')

@admin.register(Stop_numbers)
class Stop_numbersAdmin(admin.ModelAdmin):
    list_display = ('stop_number', 'stop_type')

@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ('stop', 'changed_date', 'greasing_date', 'work_done', 'work_done_date')

@admin.register(Tsw_number)
class Tsw_numberAdmin(admin.ModelAdmin):
    list_display = ('tsw_number', 'tsw_type')

@admin.register(Tsw)
class TswAdmin(admin.ModelAdmin):
    list_display = ('tsw', 'bearing_change_date', 'work_done', 'work_done_date')

