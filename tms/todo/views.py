from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView, View
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.
from .models import Task
from todo.forms import TodoForm

from django.contrib.auth.mixins import LoginRequiredMixin


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
    fields = ['task', 'desc']
    success_url = reverse_lazy('todo:items')


class Update(UpdateView):
    model = Task
    template = 'todo/task_update.html'
    success_url = reverse_lazy('blog:home')

    def get(self, request, pk):
        task = get_object_or_404(self.model, pk=pk)
        # print(blog.title)
        ctx = {'task': task.task, 'desc': task.desc}
        # print(ctx)
        return render(request, self.template, ctx)

    def post(self, request, pk):
        task = get_object_or_404(self.model, pk=pk)
        form = TodoForm(request.POST, instance=blog)
        if not form.is_valid():
            ctx = {'task': task.name, 'desc': task.desc}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)
    success_url = reverse_lazy('todo:items')


class Delete(DeleteView):
    model = Task
    fields = ['task', 'desc']
    success_url = reverse_lazy('todo:items')


@method_decorator(csrf_exempt, name='dispatch')
class Togglebool(View):
    def post(self, request, pk):
        print("Add PK", pk)
        t = get_object_or_404(Task, id=pk)
        t.done = not t.done
        try:
            print("hello")
            t.save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()

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
