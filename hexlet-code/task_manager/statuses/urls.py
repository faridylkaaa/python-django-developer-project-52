from django.urls import path
from task_manager.statuses import views

urlpatterns = [
    path('', views.IndexViewStatuses.as_view(), name="index"),
    path('create/', views.CreateViewStatus.as_view(), name="create"),
    path('<int:pk>/update/', views.UpdateViewStatus.as_view(), name="update"),
    path('<int:pk>/delete/', views.DeleteViewStatus.as_view(), name='delete')
]