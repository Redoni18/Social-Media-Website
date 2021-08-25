"""django_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as userViews
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.UserRegisterView, name = 'user-register'),
    path('login/', userViews.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', userViews.LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('user_search/', user_views.search_user_by_id, name='search-users'),
    path('profile-users/<int:pk>/', user_views.get_profile, name='users-profile'),
    path('remove/<int:pk>/', user_views.remove_followers, name="remove"),
    path('friends/<int:pk>/', user_views.add_friends, name="friends"),
    path('timeline/', user_views.timeline, name="timeline"),
    path('user-friends/<int:pk>/', user_views.get_friends, name="get_friends"),
    path('user-followers/<int:pk>/', user_views.get_followers, name="get_followers"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='home/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='home/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'),name='password_reset_complete'),
    path('home/', user_views.home, name='home'),
    path('post/', user_views.post, name='post'),
    path('messages/', user_views.message, name='messages'),
    path('',include('blogi.urls')),
    

]


if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)