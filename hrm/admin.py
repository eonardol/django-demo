from django.contrib import admin

# Register your models here.
from .models import AbsenceType
from .models import AbsenceRequest

admin.site.register(AbsenceType)
admin.site.register(AbsenceRequest)

# test
