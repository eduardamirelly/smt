from django.contrib import admin
from .models import Student, PhonesStudent, Anamnese, ImageFaceStudent

# Register your models here.

admin.site.register(Student)
admin.site.register(PhonesStudent)
admin.site.register(Anamnese)
admin.site.register(ImageFaceStudent)
