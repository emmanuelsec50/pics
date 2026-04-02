# from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.user_list),
    path('Add/', views.AddUser),
    path('Edit/<id>', views.EditUser),
    path('Delete/<eid>', views.DeleteUser),
    path('View/<eid>', views.ViewUser),
]