from rest_framework import routers
from .views import ParentViewSet, ChildViewSet,TaskViewSet
from django.urls import path, include
router=routers.DefaultRouter()
#add a new path to the default ones
router.register('parents',ParentViewSet,basename='parents')
router.register('children',ChildViewSet,basename='children')
router.register('tasks',TaskViewSet,basename='tasks')
urlpatterns=[
    path('',include(router.urls))
]