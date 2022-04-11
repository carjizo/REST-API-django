from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('user-estudiantes', views.UserProfileViewSet)
router.register('cursos', views.CourseViewSet)
router.register('matricula', views.RegistrationViewSet)
router.register('padre-familia', views.FatherFamilyViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]