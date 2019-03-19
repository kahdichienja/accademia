from django.shortcuts import render, redirect
from .models import AssignmentSubmissionForm, AssinmentType
from .forms import AssignmentForm
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.

# all Assignments
def assignments_home(request):
    if request.user.is_authenticated:
        assignments = AssignmentSubmissionForm.objects.all().order_by('-id').filter(admission_number=request.user.admission_number)
        print(assignments)
        paginator = Paginator(assignments, 5)
        page = request.GET.get('page')
        assignments = paginator.get_page(page)
    else:
        return redirect('/') 
    return render(request, "home.html", { 'assignments': assignments })  

# Assignments add
def submit_assignment_view(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AssignmentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/Assignments/home')
        else:
            form = AssignmentForm()
            return render(request, "index.html", {
                'form': form,
            })
    else:
        form = AssignmentForm()
        return render(request, "index.html", {
            'form': form,
        })
