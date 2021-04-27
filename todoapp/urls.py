from django.urls import path
from . import views

urlpatterns = [
    path('display/',views.display,name="display"),
    path('task-create/',views.task_create,name="task-create"),
    path('task/<int:pk>/',views.task_view,name="task"),
    path('update/<int:id>/',views.task_update,name="update"),
    path('delete/<int:id>/',views.task_delete,name="delete"),
    path('register/',views.register,name="register"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutuser,name="logout"),
]

