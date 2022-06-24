from django.urls import path, include
from .api import TaskList
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/tasks', TaskList, basename='api_tasks')


urlpatterns = [
   	# path('', include('app_tasks.urls'), name='tasks'),
	# path('', include('app_users.urls'), name='users'),
] + router.urls