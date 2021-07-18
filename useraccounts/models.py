from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils import timezone


class Chitiet(models.Model):
    name=models.CharField(max_length=200)
    parent =models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    macourses=models.CharField(max_length=200)
    
    def __str__(self):
        return "%s -- >  %s" %(self.parent,self.name)
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    fullname = models.CharField(max_length=200, null=True)
    account = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    avatar = models.ImageField(default='profile1.png',upload_to='studentfile',max_length=254, blank=True, null=True)


    def __str__(self):
        return self.fullname

class Category(models.Model):
    namecategory = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.namecategory

class Courses(models.Model):
    CATEGORY = (
        ('1', 'Đại Học - Cao Đẳng'),
        ('2', 'Bổ Trợ'),
        ('3', 'Luyện thi đại học'),
        ('4', 'Bồi dưỡng học sinh giỏi'),
        ('6', 'Từ lớp 6 đến lớp 9'),
        ('7', 'Luyện thi vào lớp 6'),
        ('8', 'Từ lớp 5 đến lớp 9'),
        ('9', 'Học nghe')
    )
    nameCourse = models.CharField(max_length=200, null=True)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    category =models.CharField(max_length=200, null=True, choices=CATEGORY)
    courseImg =  models.ImageField(
        upload_to='courseFile',
        max_length=254, blank=True, null=True
    )
    detail = models.TextField(default='')
    benefit = models.TextField(default='')
    makhoahoc = models.CharField(max_length=200, default="")
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
    address = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    degree = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True)
    exp = models.CharField(max_length=200, null=True)
    follow =models.CharField(max_length=200, null=True)
    course =models.CharField(max_length=200, null=True)
    avatar = models.ImageField(default='profile1.png', upload_to='teacherfile', max_length=254, blank=True, null=True)
    description = models.TextField(default='')
    review = models.TextField(default='')
    

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

class Video(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(default= "", upload_to='video_files',
                                  validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail = models.FileField(default= "", upload_to='thumbnails', validators=[
                                 FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    date_posted = models.DateTimeField(default=timezone.now)
    makhoahoc = models.CharField(max_length=200, default="")


    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user} | Created On: {self.created_on.strftime("%b %d %Y %I:%M %p")}'

class Exam(models.Model):
    exam_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.exam_name

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default="")
    marks = models.PositiveIntegerField()
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    cate = (('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4'))
    answer = models.CharField(max_length=200, choices=cate)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE, default="")
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
class Order(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.courses.nameCourse

class BlogDetail(models.Model):
    title = models.CharField(max_length=100)
    paragraph1 = models.TextField(default='')
    paragraph2 = models.TextField(default='')
    paragraph3 = models.TextField(default='')
    img1 = models.ImageField(default='', upload_to='blogfile', max_length=254, blank=True, null=True)
    img2 = models.ImageField(default='', upload_to='blogfile', max_length=254, blank=True, null=True)
    img3 = models.ImageField(default='', upload_to='blogfile', max_length=254, blank=True, null=True)
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
