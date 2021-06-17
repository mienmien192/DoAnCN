from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(OrderCourse)
admin.site.register(OrderItem)