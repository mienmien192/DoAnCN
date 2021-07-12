from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import *
from . import forms
from .forms import CreateUserForm, StudentForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
import json
from django.urls import reverse
from datetime import date, timedelta

from tkinter import messagebox as tkMessageBox


# app = Flask(__name__)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT']=465
# app.config['MAIL_USERNAME']="projectfood21@gmail.com"
# app.config['MAIL_PASSWORD']="tranminhchien"
# app.config['MAIL_USER_TLS']=False
# app.config['MAIL_USER_SSL']=True

# mail=Mail(app)


# User = settings.AUTH_USER_MODEL


def contact(request):
    if request.method == "POST":
        msg = request.POST.get('message')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        name = request.POST.get('name')
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': msg
        }
        message = '''
        Username :{}
        New message:{}
        From :{}
        '''.format(data['name'], data['message'], data['email'])
        send_mail(data['subject'], message, '', ['projectdoan21@gmail.com'])
        tkMessageBox.showinfo(title="Thông báo", message="Yêu cầu của bạn đã được gửi đi")
        # Thay doi gmail admin

    return render(request, "accounts/email.html", {})


def paypal(request):
    return render(request, 'courses/paypal.html')


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
    if 'searched' in request.GET:
        searched = request.GET['searched']
        courses = Courses.objects.filter(nameCourse__icontains=searched)
        teachers = Teacher.objects.filter(fullname__icontains=searched)
        category = Category.objects.filter(namecategory__icontains=searched)
    else:
        courses_python = Courses.objects.filter(category=1)
        courses_php = Courses.objects.filter(category=2)
        courses = Courses.objects.all()
        teachers = Teacher.objects.all()
        category = Category.objects.all()
    context = {'teachers': teachers, 'courses': courses, 'category': category, 'courses_python': courses_python,
               'courses_php': courses_php}
    return render(request, 'accounts/base.html', context)


def category(request, id):
    libcourse = LibCourse.objects.filter(category=id)
    courses = Courses.objects.filter(category=id)
    context = {'courses': courses, 'libcourse': libcourse}
    return render(request, 'accounts/category.html', context)


def getcategory(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'accounts/sectionhero.html', context)


def dashboard(request):
    teacher = Teacher.objects.all()
    student = Student.objects.all()

    context = {'teacher': teacher, 'student': student}
    return render(request, 'accounts/dashboard.html', context)


def courses(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'accounts/courses.html', context)


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
    student = Student.objects.all()
    context = {'student': student}
    return render(request, 'login/profile.html', context)


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
    context = {'courses': courses}
    return render(request, 'courses/course.html', context)
    # store


def cart(request):
    if request.user.is_authenticated:
        student = request.user.student
        order, created = OrderCourse.objects.get_or_create(student=student, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0}

    context = {'items': items, 'order': order}
    return render(request, 'courses/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        student = request.user.student
        order, created = OrderCourse.objects.get_or_create(student=student, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'courses/checkout.html', context)


def courseGrid(request):
    libcourse = LibCourse.objects.all()
    paginator = Paginator(libcourse, 4)
    pageNumber = request.GET.get('page')
    try:
        nameLCourse = paginator.page(pageNumber)
    except PageNotAnInteger:
        nameLCourse = paginator.page(1)
    except EmptyPage:
        nameLCourse = paginator.page(paginator.num_pages)
    return render(request, 'courses/coursesGrid.html', {'libcourse': libcourse, 'nameLCourse': nameLCourse})


def infoHocPhi(request):
    context = {}
    return render(request, 'accounts/infoHocPhi.html')


def updateItem(request):
    data = json.loads(request.body)
    courseId = data['courseId']
    action = data['action']

    print('Action:', action)
    print('courseId:', courseId)

    student = request.user.student
    courses = Courses.objects.get(id=courseId)

    order, created = OrderCourse.objects.get_or_create(student=student, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, courses=courses)

    orderItem.save()

    return JsonResponse('Item was added.', safe=False)


def detailTeacher(request, id):
    teachers = Teacher.objects.get(id=id)
    context = {'teachers': teachers}

    return render(request, 'courses/detailTeacher.html', context)


def detailCourse(request, id):
    courses = Courses.objects.get(id=id)
    data = Chitiet.objects.filter(macourses=id)
    videos = Video.objects.filter(makhoahoc=id)

    context = {'courses': courses, 'videos': videos, 'data': data}

    return render(request, 'courses/detailCourse.html', context)


def detailVideo(request, pk):
    video = Video.objects.filter(pk=pk)

    if request.method == "post":
        form = CommentForm(request.post, user=request.user, video=video)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()
    context = {
        'video': video,
        'form': form,
    }

    return render(request, 'courses/detailVideo.html', context)


# student_exam_view

def tuLuyen(request):
    exam = Exam.objects.all()
    context = {'exam': exam}
    return render(request, 'exam/tuluyen.html', context)


def take_exam_view(request, pk):
    exam = Exam.objects.get(id=pk)
    total_questions = Question.objects.all().filter(exam=exam).count()
    questions = Question.objects.all().filter(exam=exam)
    total_marks = 0
    for q in questions:
        total_marks = total_marks + q.marks
    return render(request, 'exam/take_exam.html',
                  {'exam': exam, 'total_questions': total_questions, 'total_marks': total_marks})

@login_required(login_url='LOGIN_REDIRECT_URL')
def start_exam_view(request, pk):
    exam = Exam.objects.get(id=pk)
    questions = Question.objects.all().filter(exam=exam)
    if request.method == 'POST':
        pass
    response = render(request, 'exam/start_exam.html', {'exam': exam, 'questions': questions})
    response.set_cookie('exam_id', exam.id)
    return response


def calculate_marks_view(request):
    if request.COOKIES.get('exam_id') is not None:
        exam_id = request.COOKIES.get('exam_id')
        exam = Exam.objects.get(id=exam_id)

        total_marks = 0
        questions = Question.objects.all().filter(exam=exam)
        for i in range(len(questions)):

            selected_ans = request.COOKIES.get(str(i + 1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = Student.objects.get(user_id=request.user.id)
        result = Result()
        result.marks = total_marks
        result.exam = exam
        result.student = student
        result.save()

        return HttpResponseRedirect('view-result')


def view_result_view(request):
    exam = Exam.objects.all()
    return render(request, 'exam/view_result.html', {'exam': exam})


def check_marks_view(request, pk):
    exam = Exam.objects.get(id=pk)
    student = Student.objects.get(user_id=request.user.id)
    results = Result.objects.all().filter(exam=exam).filter(student=student)
    return render(request, 'exam/check_marks.html', {'results': results})


def student_marks(request):
    exam = Exam.objects.all()
    return render(request, 'exam/student_marks.html', {'exam': exam})


def paymentComplete(request):
    body = json.loads(request.body)

    print('body:', body)

    courses = Courses.objects.filter(id=body['coursesId'])

    for courses in courses:
        Order.objects.create(
            courses=courses
        )
    return JsonResponse('Thanh toan thanh cong ', safe=False)


def delete(request, id):
    if request.method == "POST":
        if request.user.is_authenticated:
            student = request.user.student
            order, created = OrderCourse.objects.get_or_create(student=student, complete=False)
            items = order.orderitem_set.get(pk=id)
            items.delete()
    return HttpResponseRedirect(reverse('cart'))


def addExam(request):
    questionForm = forms.QuestionForm()
    if request.method == 'POST':
        questionForm = forms.QuestionForm(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=False)
            exam = Exam.objects.get(id=request.POST.get('examID'))
            question.exam = exam
            question.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/viewExam')
    context = {'questionForm': questionForm}
    return render(request, 'exam/add_exam.html', context)


def adminQuestion(request):
    return render(request, 'exam/admin_question.html')


def viewExam(request):
    exam = Exam.objects.all()
    return render(request, 'exam/viewExam.html', {'exam': exam})


def viewQuestion(request, pk):
    questions = Question.objects.all().filter(exam_id=pk)
    return render(request, 'exam/viewQuestion.html', {'questions': questions})


def deleteQuestion(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/viewExam')