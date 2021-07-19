from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views
from .views import edtechBot
urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('courses/', views.courses, name="courses"),
    path('student/', views.student, name="student"),
    path('teacher/', views.Teachers, name="teacher"),
    path('login/', views.loginUser, name="login"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('accountst/', views.accountSettings, name="accountst"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='login/password_reset.html'),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_sent.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_form.html'),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_done.html'),
         name="password_reset_complete"),

    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('tuluyen/', views.tuLuyen, name="tuluyen"),
    path('hocphi/', views.infoHocPhi, name="hocphi"),
    path('courseGrid/', views.courseGrid, name="courseGrid"),
    path('update_item/', views.updateItem, name="update_item"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.Blog, name="blog"),
    path('blogDetail/<int:id>', views.blogDetail, name="blogDetail"),
    path('detailTeacher/<int:id>', views.detailTeacher, name="detailTeacher"),
    path('detailCourse/<int:id>', views.detailCourse, name="detailCourse"),
    path('detailVideo/<int:pk>', views.detailVideo, name="detailVideo"),
    path('take-exam/<int:pk>', views.take_exam_view, name='take-exam'),
    path('start-exam/<int:pk>', views.start_exam_view, name='start-exam'),
    path('calculate-marks', views.calculate_marks_view, name='calculate-marks'),
    path('view-result', views.view_result_view, name='view-result'),
    path('category/<int:id>', views.category, name="category"),
    path('paypal/', views.paypal, name="paypal"),
    path('complete/', views.paymentComplete, name="complete"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('addExam/', views.addExam, name="addExam"),
    path('adminQuestion/', views.adminQuestion, name="adminQuestion"),
    path('viewExam/', views.viewExam, name="viewExam"),
    path('viewQuestion/<int:pk>', views.viewQuestion, name='viewQuestion'),
    path('deleteQuestion/<int:pk>', views.deleteQuestion, name='deleteQuestion'),
    path('check-marks/<int:pk>', views.check_marks_view, name='check-marks'),
    path('student-marks', views.student_marks, name='student-marks'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add/', views.add, name='add'),
    path('Xoafile_student/<int:pk>', views.Xoafile_student, name='Xoafile_student'),
    path('Xoafile_khoahoc/<int:pk>', views.Xoafile_khoahoc, name='Xoafile_khoahoc'),
    path('Xoafile_teacher/<int:pk>', views.Xoafile_teacher, name='Xoafile_teacher'),
    url(r'^9a5bf40a28d78050ceddc57c70c5b79f7c38d4ea2f83ed0f10/?$', edtechBot.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
