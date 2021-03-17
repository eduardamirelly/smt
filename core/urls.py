from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.loginMatriculationStudent, name='login-matriculation'),
    path('import/excel/', views.importFile, name='upload-file'),
    path('list/students/', views.listStudents, name='list-students'),
    path('student/<str:student>/', views.dataStudent, name='data-student'),
    path('student/<str:student>/instant/image/', views.imageInstant, name='image-instant'),
    path('anamnese/register/<str:student>/', views.registerAnamneseStudent, name='register-anamnese'),
    path('anamnese/list/', views.listAnamneses, name='list-anamneses'),
    path('anamnese/detalhar/<int:pk>/', views.showAnamnese, name='show-anamnese'),
    path('anamnese/excluir<int:pk>/', views.deleteAnamnese, name='delete-anamnese'),
    path('entrada', views.enterCampi, name='enter-campi'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
