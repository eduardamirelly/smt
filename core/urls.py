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
    path('student/<str:student>/delete/image/<int:pk>', views.deleteImageInstant, name='delete-image'),
    path('student/<str:student>/anamnese/list/', views.listAnamneses, name='list-anamneses'),
    path('student/<str:student>/anamnese/list/<int:pk>/', views.showAnamnese, name='show-anamnese'),
    path('student/<str:student>/anamnese/register/', views.registerAnamneseStudent, name='register-anamnese'),
    path('student/<str:student>/anamnese/delete/<int:pk>/', views.deleteAnamnese, name='delete-anamnese'),
    path('entry/', views.enterCampi, name='enter-campi'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
