"""
URL configuration for TKPM_21880128_Timetable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers

from classrooms.views import (
    PeriodViewSet,
    SubjectTeacherViewSet,
    ClassRoomViewSet,
    SubjectViewSet,
    PeriodAdjustmentViewSet,
)
from schools.views import (TeacherViewSet, SchoolViewSet)
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"schools", SchoolViewSet)
router.register(r"classrooms", ClassRoomViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"subjects", SubjectViewSet)
router.register(r"subject-teachers", SubjectTeacherViewSet)
router.register(r"periods", PeriodViewSet)
router.register(r"period-adjustments", PeriodAdjustmentViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v0/", include(router.urls)),
]
