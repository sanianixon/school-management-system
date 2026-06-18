from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import School, Student
from .forms import SchoolForm, StudentForm
from .serializers import (
    SchoolSerializer,
    StudentSerializer,
    SchoolWithStudentsSerializer,
)


def dashboard(request):
    total_schools = School.objects.count()
    total_students = Student.objects.count()

    return render(
        request,
        'dashboard.html',
        {
            'total_schools': total_schools,
            'total_students': total_students
        }
    )


# SCHOOL CRUD

def school_list(request):
    return render(request, 'school/list.html')


def school_create(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = SchoolForm()

    return render(request, 'school/form.html', {'form': form})


def school_update(request, pk):
    school = get_object_or_404(School, pk=pk)

    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)

        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = SchoolForm(instance=school)

    return render(request, 'school/form.html', {'form': form})


def school_delete(request, pk):
    school = get_object_or_404(School, pk=pk)
    school.delete()

    return redirect('school_list')


# STUDENT CRUD

def student_list(request):
    students = Student.objects.select_related('school').all()

    return render(request, 'student/list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'student/form.html', {'form': form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student/form.html', {'form': form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()

    return redirect('student_list')


# API VIEWS

@api_view(['GET'])
def school_detail_api(request, pk):
    try:
        school = School.objects.get(pk=pk)
        serializer = SchoolSerializer(school)

        return Response({
            'status': True,
            'message': 'School fetched successfully',
            'data': serializer.data
        })

    except School.DoesNotExist:
        return Response({
            'status': False,
            'message': 'School not found',
            'data': None
        })


@api_view(['GET'])
def student_detail_api(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)

        return Response({
            'status': True,
            'message': 'Student fetched successfully',
            'data': serializer.data
        })

    except Student.DoesNotExist:
        return Response({
            'status': False,
            'message': 'Student not found',
            'data': None
        })


@api_view(['GET'])
def school_students_api(request, pk):
    try:
        school = School.objects.get(pk=pk)
        serializer = SchoolWithStudentsSerializer(school)

        return Response({
            'status': True,
            'message': 'School with students fetched successfully',
            'data': serializer.data
        })

    except School.DoesNotExist:
        return Response({
            'status': False,
            'message': 'School not found',
            'data': None
        })


@api_view(['GET'])
def school_list_api(request):
    schools = School.objects.all()
    serializer = SchoolSerializer(schools, many=True)

    return Response({
        'status': True,
        'message': 'Schools fetched successfully',
        'data': serializer.data
    })