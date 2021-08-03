from django.contrib import admin
from .models import WRide, WHead, Transport, Stop, InlineStop, Route, ExpenseGroup, Unit

admin.site.register(WRide)
admin.site.register(WHead)
admin.site.register(Transport)
admin.site.register(Stop)
admin.site.register(ExpenseGroup)
admin.site.register(Unit)
#admin.site.register(InlineStop)


class StopsInline(admin.TabularInline):
    model = InlineStop
    extra = 0
    min_num = 2


class RouteAdmin(admin.ModelAdmin):
    inlines=[StopsInline]


admin.site.register(Route, RouteAdmin)