from django.contrib import admin
from .models import Accident
from .models import Victim
from .models import Municipality
# Register your models here.

admin.site.register(Accident)
admin.site.register(Victim)
admin.site.register(Municipality)