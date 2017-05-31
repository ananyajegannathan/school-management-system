from django.shortcuts import render
from rest_framework import viewsets
from school.models import Student, Teacher, Admin, Grade, Section
from school.serializers import (StudentSerializer, TeacherSerializer, AdminSerializer,
GradeSerializer, SectionSerializer)
import django_filters.rest_framework

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','subject','email','phone_no')

class AdminViewSet(viewsets.ModelViewSet):
	queryset = Admin.objects.all()
	serializer_class = AdminSerializer

class GradeViewSet(viewsets.ModelViewSet):
	queryset = Grade.objects.all()
	serializer_class = GradeSerializer

class SectionViewSet(viewsets.ModelViewSet):
	queryset  = Section.objects.all()
	serializer_class = SectionSerializer