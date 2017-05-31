from django.db import models


class Teacher(models.Model):
	name = models.CharField(primary_key=True, max_length=50)
	subject = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	dob = models.DateField()
	email = models.EmailField(max_length=100)
	phone_no = models.IntegerField()

	def __str__(self):
		return self.name

class Grade(models.Model):
	std = models.CharField(max_length=3, default='DEFAULT VALUE', primary_key=True)
	class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	no_of_students = models.IntegerField()

	def __str__(self):
		return self.std

class Section(models.Model):
	std = models.ForeignKey(Grade, on_delete=models.CASCADE, primary_key=True,  default='DEFAULT VALUE')
	class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.std)

class Student(models.Model):
	id_no = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	roll_no = models.IntegerField()
	std = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='students')
	address = models.CharField(max_length=200)
	dob = models.DateField()
	father_name = models.CharField(max_length=50, default='DEFAULT VALUE', blank=True, null=True)
	mother_name = models.CharField(max_length=50, default='DEFAULT VALUE', blank=True, null=True)
	email = models.EmailField(max_length=100)
	phone_no = models.IntegerField()

class Admin(models.Model):
	name = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	dob = models.DateField()
	email = models.EmailField(max_length=100)
	phone_no = models.IntegerField()










