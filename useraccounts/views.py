from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import CreateUserForm, StudentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import json
User = settings.AUTH_USER_MODEL

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'login/register.html', context)


def home(request):
    teachers = Teacher.objects.all()
    courses = Courses.objects.all()
    context = {'teachers': teachers, 'courses': courses}
    return render(request, 'accounts/base.html', context)


def dashboard(request):
    courses = Courses.objects.all()
    student = Student.objects.all()

    context = {'courses': courses, 'student': student}
    return render(request, 'accounts/dashboard.html', context)


def courses(request):
    courses = Courses.objects.all()
    return render(request, 'accounts/courses.html', {'courses': courses})


def student(request, pk_test):
    student = Student.objects.get(id=pk_test)
    context = {'student': student}
    return render(request, 'accounts/student.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Tài khoản hoặc mật khẩu không đúng')

    context = {}

    return render(request, 'login/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def profile(request):
    return render(request, 'login/profile.html')


def accountSettings(request):
    student = request.user.student
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'login/account_setting.html', context)

def course(request):
    courses = Courses.objects.all()
    context = {'courses':courses}
    return render(request, 'courses/course.html', context)
    # store

def cart(request):
    if request.user.is_authenticated:
        student = request.user.student
        order, created = OrderCourse.objects.get_or_create(student=student, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total':0}

    context = {'items':items, 'order':order}
    return render(request, 'courses/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        student = request.user.student
        order, created = OrderCourse.objects.get_or_create(student=student, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total':0}
    context = {'items':items, 'order':order}
    return render(request, 'courses/checkout.html', context)

def courseGrid(request):
    libcourse = LibCourse.objects.all()
    context = {}
    return render(request, 'courses/coursesGrid.html',{'libcourse':libcourse})
def tuLuyen(request):
    context = {}
    return render(request, 'exam/tuluyen.html')

def infoHocPhi(request):
    context = {}
    return render(request, 'accounts/infoHocPhi.html')

def updateItem(request):
    data = json.loads(request.data)
    courseId = data['courseId']
    action = data['action']

    print('Action:', action)
    print('courseId:', courseId)
    return JsonResponse('Item was added.', safe=False)