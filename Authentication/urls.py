from django.urls import path
from . import views
from .views import PasswordsChangeView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name="logout"),
    path('profile', views.UserChangeProfile.as_view(), name="profile"),
    path('github', views.github, name='github'),
    path('facebook', views.facebook, name='facebook'),
    path('twitter', views.twitter, name='twitter'),
    path('send_message', views.send_message, name='message'),
    path('change_password', PasswordsChangeView.as_view(
        template_name='profile/change-password.html'), name="change_password"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
