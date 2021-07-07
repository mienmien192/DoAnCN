from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(OrderCourse)
admin.site.register(OrderItem)
admin.site.register(Teacher)
admin.site.register(LibCourse)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Exam)
admin.site.register(Category)

 
