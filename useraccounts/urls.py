from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


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
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)