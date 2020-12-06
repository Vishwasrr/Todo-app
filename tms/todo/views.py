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
from django.db.models import Q


class Index(ListView):
    model = Task

    def get(self, request):
        strval = request.GET.get("search", False)
        if strval:
            # Simple title-only search
            # objects = Task.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            query = Q(task__contains=strval)
            items = Task.objects.filter(query).select_related()
        else:
            # try both versions with > 4 posts and watch the queries that happen
            items = Task.objects.all()
            # objects = Task.objects.select_related().all().order_by('-updated_at')[:10]
    # template_name = 'todo/todo_index.html'

    # def get(self, request):
    #     # items = Task.objects.all().count()
    #     items = Task.objects.all()

        ctx = {'task_list': items}
        return render(request, 'todo/task_list.html', ctx)


class Details(LoginRequiredMixin, DetailView):
    model = Task
    # template_name = 'todo/todo_details.html'

    # def get(self, request, pk):
    #     item = Task.objects.get(id=pk)
    #     context = {'item': item}
    #     return render(request, self.template_name, context)


def Create(request):
    form = TodoForm(request.POST)
    form.save()
    return HttpResponse()


class Update(LoginRequiredMixin, UpdateView):
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


class Delete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = ['task', 'desc']
    success_url = reverse_lazy('todo:items')


@method_decorator(csrf_exempt, name='dispatch')
class Togglebool(LoginRequiredMixin, View):
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
