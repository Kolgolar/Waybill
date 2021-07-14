from django.contrib import admin
from .models import WRide, WHead, Transport, Stop, InlineStop, Route

admin.site.register(WRide)
admin.site.register(WHead)
admin.site.register(Transport)
admin.site.register(Stop)


class StopsInline(admin.TabularInline):
    model = InlineStop
    extra = 0
    min_num = 2


class RouteAdmin(admin.ModelAdmin):
    inlines=[StopsInline]


admin.site.register(Route, RouteAdmin)


#https://coderoad.ru/27081815/%D0%BA%D0%B0%D0%BA-%D0%BB%D1%83%D1%87%D1%88%D0%B5-%D0%B2%D1%81%D0%B5%D0%B3%D0%BE-%D0%BD%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C-%D0%BF%D0%BE%D0%BB%D0%B5-%D1%81%D0%BE-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%BE%D0%BC-%D0%B2-django