from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .models import Task
from .forms import TaskForm
from django.contrib.auth import logout
# 🔐 Custom Login View with Success Message
class CustomLoginView(LoginView):
    template_name = 'todo/login.html'

    def form_valid(self, form):
        messages.success(self.request, "Login successful!")
        return super().form_valid(form)

# 🧾 Register New User
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

# 🏠 Index Page (List + Add Task)
@login_required
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")
            return redirect('index')

    return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})

# ✏ Edit Task
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated!")
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/edit_task.html', {'form': form, 'task': task})

# ❌ Delete Task
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.warning(request, "Task deleted.")
    return redirect('index')

# ✅ Mark Task as Completed
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    messages.info(request, "Task marked as complete.")
    return redirect('index')


@login_required 
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


