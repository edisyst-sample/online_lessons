from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, LessonViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
