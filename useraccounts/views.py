from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import CreateUserForm, StudentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import json


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
    return render(request, 'accounts/base.html')


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
    context = {}
    return render(request, 'courses/cart.html')

def checkout(request):
    context = {}
    return render(request, 'courses/checkout.html')