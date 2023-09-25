from django.shortcuts import render, redirect, get_object_or_404
from .models import  ProgrammerModel, Project
from .forms import ProjectForm

def programmer_list(request):
    programmers = ProgrammerModel.objects.all()
    return render(request, 'programmer_list.html', {'programmers':programmers})

def programmer_detail(request, programmer_id):
    programmer = get_object_or_404(ProgrammerModel, id=programmer_id)
    return render(request, 'programmer_detail.html', {'programmer':programmer})

def add_project(request, programmer_id):
    programmer = get_object_or_404(ProgrammerModel, id=programmer_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.programmer = programmer
            project.save()
            return redirect('programmer_detail', programmer_id = programmer.id)
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'programmer':programmer, 'form':form})
