from django.urls import path

from .views import Create, Index, Details, Update, Delete
from . import views

app_name = 'todo'
urlpatterns = [
    path('', Index.as_view(), name='items'),
    path('create/', Create, name='create'),
    path('<int:pk>', Details.as_view(), name='detail'),
    path('<int:pk>/update/', Update.as_view(), name='update'),
    path('<int:pk>/delete/', Delete.as_view(), name='delete'),
    path('<int:pk>/toggle/', 
        views.Togglebool.as_view(), name='toggle'),
]
