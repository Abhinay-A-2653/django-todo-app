from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':  # If the form is submitted
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('task_list')  # Redirect to the task list page after successful save
    else:
        form = TaskForm()  # Empty form for GET request
    
    return render(request, 'add_tasks.html', {'form': form})

def toggle_task_status(request, task_id):
    task = Task.objects.get(id=task_id)  # Retrieve the task by its ID
    task.done = not task.done  # Toggle the 'done' field value
    task.save()  # Save the updated task back to the database
    return redirect('task_list')  # Redirect back to the task list

def delete_task(request, task_id):
    # Fetch the task by its ID or return 404 if not found
    task = get_object_or_404(Task, id=task_id)
    task.delete()  # Delete the task from the database
    return redirect('task_list')  # Redirect back to the task list
