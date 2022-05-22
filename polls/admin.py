from django.contrib import admin

# Register your models here.

from .models import TradePoint
from .models import TradePointType
from .models import SomeStore
from .models import DepartmentStore


admin.site.register(TradePointType)
admin.site.register(TradePoint)
admin.site.register(SomeStore)
admin.site.register(DepartmentStore)
