from django.db import models
from datetime import date
# Create your models here.
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
    nb_chields=models.PositiveSmallIntegerField(default=1)
    class Meta:
        db_table='parent'
    def __str__(self):
        #return self.firstName,', ',self.lastName,', ',self.birthdate
        #or
        #return f'firstName = {self.firstName}, lastName = {self.lastName}, birthdate = {self.birthdate}'
        #or
        return 'firstName = %s, lastName = %s, birthdate = %s' % self.firstName,self.lastName,self.birthdate

class Child(Person):
    level=models.CharField(max_length=50,choices=[('1ST','first study class'),('2ND','second study class'),('3RD','third study class')],default='1ST')
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)