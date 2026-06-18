from rest_framework import serializers
from .models import School, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class SchoolWithStudentsSerializer(serializers.ModelSerializer):
    students = StudentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = School
        fields = [
            'id',
            'name',
            'students'
        ]