"""todowoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from news import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Todos
    path('create/', views.createnews, name='createnews'),
    path('current/', views.currentnews, name='currentnews'),
    path('archives/', views.archivednews, name='archivednews'),
    path('news/<int:news_id>', views.viewnews, name='viewnews'),
    path('news/<int:news_id>/detail', views.detail, name='detail'),
    path('news/<int:news_id>/delete', views.deletenews, name='deletenews'),
    path('news/<int:news_id>/archive', views.archivenews, name='archivenews'),
    path('news/<int:news_id>/dearchive', views.dearchivenews, name='dearchivenews'),
    path('news/<int:news_id>/archives/delete', views.deletenews_archives, name='deletenews_archives'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
