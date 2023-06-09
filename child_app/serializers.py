from rest_framework import serializers
from .models import Child, Parent, Task
#Serialize all fields of the model Parent
#this class will be used each time we want to serialize a Parent object to JSON
#or deserialize a JSON to a Parent object
class ParentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parent
        fields = '__all__'
        
class ChildSerializer(serializers.ModelSerializer):
    #serialize the parent field using the ParentSerializer
    #parent is a foreign key to the model Parent
    #parent = ParentSerializer()
    class Meta:
        model = Child
        #serialize only the id, name, age and parent fields
        fields = ('id', 'firstName','lastName', 'birthdate', 'parent')

class TaskSerializer(serializers.ModelSerializer):
    #serialize the child field using the ChildSerializer
    #child is a foreign key to the model Child
    #child = ChildSerializer()
    class Meta:
        model = Task
        fields = '__all__'
    