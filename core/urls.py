from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('import/excel/', views.importFile, name='upload-file'),
    path('list/students', views.listStudents, name='list-students'),
    path('editor/', views.editorStudent, name='editor-student'),
    path('', views.loginMatriculationStudent, name='login-matriculation'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)