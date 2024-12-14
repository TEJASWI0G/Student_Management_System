from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from.forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'students/index.html',{
        'students' : Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk = id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Save the form data as a new Student instance
            form.save()

            # Render success message
            return render(request, 'students/add.html', {
                'form': StudentForm(),  # Render an empty form after saving
                'success': True
            })
    else:
        # Handle GET request: render the form
        form = StudentForm()

    # Render the form for both invalid POST and GET requests
    return render(request, 'students/add.html', {
        'form': form
    })

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk = id)
        form = StudentForm(request.POST, instance= student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk = id)
        form = StudentForm(instance = student)
    return render(request, 'students/edit.html', {
        'form': form,
    })

def delete(request,id):
    if request.method == 'POST':
        student = Student.objects.get(pk = id)
        student.delete()
        return HttpResponseRedirect(reverse('index'))
        