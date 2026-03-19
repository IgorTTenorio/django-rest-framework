from escola import views
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('estudantes', views.EstudanteViewSet, basename='Estudantes')
router.register('cursos', views.CursoViewSet, basename='Cursos')
router.register('matriculas', views.MatriculaViewSet,basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', views.ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', views.ListaMatriculaCurso.as_view()),
]