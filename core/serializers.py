from rest_framework import serializers
from .models import Student, PhonesStudent, ImageFaceStudent, Anamnese, Entry

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class PhonesStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhonesStudent
        fields = '__all__'
        
class ImageFaceStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFaceStudent
        fields = '__all__'

class AnamneseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anamnese
        fields = '__all__'

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
