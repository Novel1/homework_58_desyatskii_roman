from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_view'),
    path('add_task/', views.TaskAdd.as_view(), name='add_view'),
    path('task/<int:pk>/update', views.TaskUpdateView.as_view(), name='task_update'),
    path('article/<int:pk>/delete/', views.DeleteTaskView.as_view(), name='delete_view'),
    path('article/<int:pk>/confirm_delete/', views.DeleteTaskView.as_view(), name='confirm_delete')
]