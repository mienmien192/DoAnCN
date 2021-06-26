from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    fullname = models.CharField(max_length=200, null=True)
    account = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    avatar = models.ImageField(default='profile1.png',upload_to='studentfile',max_length=254, blank=True, null=True)
    comment = models.TextField(default='')

    def __str__(self):
        return self.fullname

class Courses(models.Model):
    CATEGORY = (
        ('1', 'DH-CD'),
        ('2', 'Bo tro'),
        ('3', 'luyen thi DH'),
        ('4', 'Boi duong HSG'),
        ('6', 'Lop6-9'),
        ('7', 'Luyen thi vao 6'),
        ('8', 'Lop1-5'),
        ('9', 'Hoc nghe')
    )
    nameCourse = models.CharField(max_length=200, null=True)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    category =models.CharField(max_length=200, null=True, choices=CATEGORY)
    courseImg =  models.ImageField(
        upload_to='courseFile',
        max_length=254, blank=True, null=True
    )

    def __str__(self):
        return self.nameCourse
class OrderCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null = True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
class OrderItem(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(OrderCourse, on_delete=models.SET_NULL, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True)

    @property
    def get_total(self):
        total = self.courses.price
        return total
class Teacher(models.Model):
    fullname = models.CharField(max_length=200, null=True)
    account = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(default='profile1.png', upload_to='teacherfile', max_length=254, blank=True, null=True)
    description = models.TextField(default='')
    def __str__(self):
        return self.fullname

class LibCourse(models.Model):
    CATEGORY = (
        ('1', 'DH-CD'),
        ('2', 'Bo tro'),
        ('3', 'luyen thi DH'),
        ('4', 'Boi duong HSG'),
        ('6', 'Lop6-9'),
        ('7', 'Luyen thi vao 6'),
        ('8', 'Lop1-5'),
        ('9', 'Hoc nghe')
    )
    nameLCourse = models.CharField(max_length=200, null=True)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    discount = models.CharField(max_length=200, null=True)
    courseImg = models.ImageField(
        upload_to='courseFile',
        max_length=254, blank=True, null=True
    )