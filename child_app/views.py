from django.shortcuts import render
from rest_framework import viewsets
from .models import Child, Parent
from .serializers import ChildSerializer, ParentSerializer
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
    #if not specified all http methods are allowed
    http_method_names=['get', 'post',]