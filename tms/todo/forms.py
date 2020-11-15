from django.forms import ModelForm
from todo.models import Task


# Create the form class.
class TodoForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
