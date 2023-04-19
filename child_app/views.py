from django.shortcuts import render
from rest_framework import viewset
from rest_framework.decorators import action
from .models import Child, Parent, Task
from .serializers import ChildSerializer, ParentSerializer, TaskSerializer
# Create your views here.
# Implements CRUD (CREATE READ UPDATE DELETE) operations on models Child and Parent`
# using viewsets.ModelViewSet from rest_framework
class ParentViewSet(viewsets.ModelViewSet):
    queryset=Parent.objects.all()
    serializer_class=ParentSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset=Child.objects.all()
    serializer_class=ChildSerializer
    #the http_method_names attribute is used to specify the HTTP methods
    #that are allowed for the view
    #this attribute is optional
    #if not specified http methods allowed are GET, POST, PUT, PATCH, DELETE
    #http_method_names=['get', 'post',]

    #customize methods:
    #get the list of children of a parent
    @action(detail=True, methods=['get'])
    def parent_children(self, request, pk=None):
        pass

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
   