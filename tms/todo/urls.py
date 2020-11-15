from django.urls import path

from .views import Create, Index, Details, Update, Delete

app_name = 'todo'
urlpatterns = [
    path('create/', Create.as_view(), name='create'),
    path('', Index.as_view(), name='items'),
    path('<int:pk>', Details.as_view(), name='detail'),
    path('<int:pk>/update/', Update.as_view(), name='update'),
    path('<int:pk>/delete/', Delete.as_view(), name='delete'),
]
