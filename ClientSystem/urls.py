"""ClientSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('detail/<int:id>', views.detail),
    re_path(r'^students/(?P<year>\d{4})-(?P<month>\d[1-9]|1[0-2])/$', views.student_list),
    # path('teacher/', include('teacher.urls'),kwargs={'args': 'something'}),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
]
