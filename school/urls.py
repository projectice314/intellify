from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.schoolHome, name="school_home"),

    # AUTHENTICATION
    path('school-register/', views.schoolRegister, name="school_register"),
    path('school-login/', views.schoolLogin, name="school_login"),
    path('school-logout/', views.schoolLogout, name='school_logout'),

    path('school-profile-add/', views.schoolProfileAdd, name='school_profile_add'),
    path('school-profile/', views.schoolProfile, name='school_profile'),

    path('add-subject/', views.add_subject, name="add_subject"),
    path('subjects/', views.list_subject, name="list_subject"),

    path('add-class/', views.add_classroom, name='add-class'),
    path('classrooms/', views.list_classroom, name="list_classroom"),
    path('classroom/', views.classroom_profile, name="classroom_profile"),

]