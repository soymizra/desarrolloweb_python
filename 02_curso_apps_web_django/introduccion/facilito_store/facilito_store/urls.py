from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('auth/login', views.login_view, name='login'),
	path('auth/logout', views.logout_view, name='logout'),
	path('auth/signup', views.signup_view, name='signup'),
    path('admin/', admin.site.urls),
]
