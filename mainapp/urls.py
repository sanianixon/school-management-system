from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('schools/', views.school_list, name='school_list'),
    path('schools/add/', views.school_create, name='school_create'),
    path('schools/edit/<int:pk>/', views.school_update, name='school_update'),
    path('schools/delete/<int:pk>/', views.school_delete, name='school_delete'),

    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/edit/<int:pk>/', views.student_update, name='student_update'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('api/school/<int:pk>/', views.school_detail_api, name='school_detail_api'),
    path('api/student/<int:pk>/', views.student_detail_api, name='student_detail_api'),
    path('api/school/<int:pk>/students/', views.school_students_api, name='school_students_api'),

    path('api/schools/', views.school_list_api, name='school_list_api'),
    path(
        'students/export/excel/',
        views.export_students_excel,
        name='export_students_excel'
    ),
]

path(
    'api/schools/',
    views.school_list_api,
    name='school_list_api'
),