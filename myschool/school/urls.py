from django.conf.urls import url, include
from school import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'faculty', views.TeacherViewSet)
router.register(r'admin', views.AdminViewSet)
router.register(r'grade', views.GradeViewSet)
router.register(r'class', views.SectionViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]