from django.urls import path, include
from .api import TaskList
from .views import AddTask, AddComment, StopTask, ChangeResponsible, UpdateTask
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/tasks', TaskList, basename='api_tasks')


urlpatterns = [
   	path('api/tasks/<int:pk>/', TaskList.as_view({'get': 'get', 'post': 'update'}), name='api_task'),
	path('add_task/', AddTask.as_view(), name='add_task'),
	path('api/tasks/<int:pk>/add_comment/', AddComment.as_view(), name='add_comment'),
	path('api/tasks/<int:pk>/stop_task/', StopTask.as_view(), name='stop_task'),
	path('api/tasks/<int:pk>/change_responsible/', ChangeResponsible.as_view(), name='change_responsible'),
	path('api/tasks/<int:pk>/update_task/', UpdateTask.as_view(), name='update_task'),
] + router.urls