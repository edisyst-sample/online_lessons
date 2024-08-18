from rest_framework import serializers
from .models import Teacher, Lesson, Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()  # Includi i dettagli dell'insegnante

    class Meta:
        model = Lesson
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
