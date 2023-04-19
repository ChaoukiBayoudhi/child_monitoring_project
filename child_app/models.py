from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.

#define a django Enum
#Defining a Django Enum <=> defining a new Type that have a limited set of values
class TaskState(models.TextChoices):
    NEW_TASK=('NEW','new task')
    IN_PROGRESS_TASK=('IN_PROGRESS','task in progress')
    DONE_TASK=('DONE','task done')
    CANCELED_TASK=('CANCELED','task is aborted')
    TO_DO_TASK=('TO_DO','task to do')
class Person(models.Model):
    firstName=models.CharField(max_length=50,default='')
    lastName=models.CharField(max_length=50,default='')
    photo=models.ImageField(upload_to='person_photo',blank=True,null=True)
    birthdate = models.DateField(default=date(1985,1,1))
    class Meta:
        abstract=True
    def __str__(self):
        #return self.firstName,', ',self.lastName,', ',self.birthdate
        #or
        #return f'firstName = {self.firstName}, lastName = {self.lastName}, birthdate = {self.birthdate}'
        #or
        return 'firstName = %s, lastName = %s, birthdate = %s' % self.firstName,self.lastName,self.birthdate
class Parent(Person):
    nb_children=models.PositiveSmallIntegerField(default=1)
    class Meta:
        db_table='parents'
    def __str__(self):
        #return self.firstName,', ',self.lastName,', ',self.birthdate
        #or
        #return f'firstName = {self.firstName}, lastName = {self.lastName}, birthdate = {self.birthdate}'
        #or
        #return 'firstName = %s, lastName = %s, birthdate = %s' % self.firstName,self.lastName,self.birthdate
        #return f'firstName = {self.firstName}, lastName = {self.lastName}'
        return f'id={self.id}'
class Child(Person):
    level=models.CharField(max_length=50,choices=[('1ST','first study class'),('2ND','second study class'),('3RD','third study class')],default='1ST')
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)

    class Meta:
        db_table='children'
    def __str__(self):
        return f'firstName = {self.firstName}, lastName = {self.lastName}'

    

#define the model Task:
class Task(models.Model):
    name=models.CharField(max_length=50,default='',unique=True)
    description=models.TextField(default='')
    duration=models.DurationField(default=0)
    start_date=models.DateTimeField(default=timezone.now)
    end_date=models.DateTimeField(default=timezone.now)#+timezone.timedelta(days=1))
    state=models.CharField(max_length=50,choices=TaskState.choices,default=TaskState.NEW_TASK)
    #or
    #state=models.CharField(max_length=50,choices=[('NEW','new task'),('IN_PROGRESS','task in progress'),('DONE''task done'),('CANCELED','task is aborted')],default='NEW')
    task_type=models.CharField(max_length=50,choices=[('SPORT','sport task'),('HOMEWORK','homework task'),('HOBBY','hobby task'),('OTHER','Other task type')],default='TO_DO')
    #relationships between task and child (many to one)
    child=models.ForeignKey(Child,on_delete=models.CASCADE)
    class Meta:
        db_table='tasks'
    def __str__(self):
        return self.name