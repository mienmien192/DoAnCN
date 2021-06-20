from django.urls import path
from . import views
from django.conf.urls.static import static

from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard),
    path('courses/', views.courses),
    path('student/<str:pk_test>/', views.student),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('accountst/', views.accountSettings, name="accountst"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'login/password_reset.html'),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'login/password_reset_sent.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'login/password_reset_form.html'),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'login/password_reset_done.html'),
         name="password_reset_complete"),

    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('courseGrid/', views.courseGrid, name="courseGrid"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)