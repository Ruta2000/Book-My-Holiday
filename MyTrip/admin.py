from django.contrib import admin

# Register your models here.
from .models import *
from .models import Cities

admin.site.register(Cities)
#admin.site.register(Profile)
admin.site.register(Bus)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Tour)
admin.site.register(TripBook)



