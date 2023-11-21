from django.urls import path

from task_manager.users import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateUser.as_view(), name='create'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<int:pk>/update/', views.UpdateUser.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete')
]