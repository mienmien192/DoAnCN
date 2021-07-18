from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(OrderCourse)
admin.site.register(OrderItem)
admin.site.register(Teacher)
admin.site.register(LibCourse)


admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Exam)
admin.site.register(Category)
admin.site.register(Chitiet)
admin.site.register(BlogDetail)

class CommentInLine(admin.TabularInline):
    model = Comment
    list_display = ['user', 'comment', 'created_on']
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_posted']
    list_filter = ['date_posted']
    search_fields = ['id']
    inlines = [CommentInLine]
admin.site.register(Video, VideoAdmin)