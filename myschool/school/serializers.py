from rest_framework import serializers
from school.models import Student, Teacher, Admin, Grade, Section


class StudentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Student
		fields = ('url','id_no','name','roll_no','std','address','dob','father_name','mother_name','email','phone_no')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Teacher
		fields = ('url','name','subject','address','dob','email','phone_no')

class AdminSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Admin
		fields = ('url','name','position','address','dob','email','phone_no')

class GradeSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(
        view_name='section-detail',
        # lookup_field='slug'
        )
	class Meta:
		model = Grade
		fields = ('url','std','class_teacher','no_of_students')

class SectionSerializer(serializers.ModelSerializer):
	students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='student-detail')

	class Meta:
		model = Section
		fields = ('std','class_teacher','students')

