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
    path('api/studentlist/', views.StudentList.as_view(), name='student-list'),
    path('api/phoneslist/', views.PhonesStudentList.as_view(), name='phones-list'),
    path('api/facestudentlist/', views.ImageFaceStudentList.as_view(), name='image_face-list'),
    path('api/anamneselist/', views.AnamneseList.as_view(), name='anamnese-list'),
    path('api/entrylist/', views.EntryList.as_view(), name='entry-list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
