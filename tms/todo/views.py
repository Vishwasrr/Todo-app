from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
# Create your views here.
from .models import Task
from todo.forms import TodoForm


class Index(ListView):
    model = Task
    # template_name = 'todo/todo_index.html'

    # def get(self, request):
    #     # items = Task.objects.all().count()
    #     items = Task.objects.all()

    #     ctx = {'items': items}
    # return render(request, 'todo/todo_list.html', ctx)


class Details(DetailView):
    model = Task
    # template_name = 'todo/todo_details.html'

    # def get(self, request, pk):
    #     item = Task.objects.get(id=pk)
    #     context = {'item': item}
    #     return render(request, self.template_name, context)


class Create(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo:items')


class Update(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo:items')


class Delete(DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo:items')

# class Create(CreateView):
#     template_name = 'todo/todo_form.html'
#     success_url = reverse_lazy('todo:items')

#     def get(self, request):
#         form = TodoForm()
#         ctx = {'form': form}
#         return render(request, self.template_name, ctx)

#     def post(self, request):
#         form = TodoForm(request.POST)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template_name, ctx)

#         todo = form.save()
#         return redirect(self.success_url)
    # def get_object(self):
