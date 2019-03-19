from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import NotesUpload, University


# Create your views here.

# Assignments add
def notes_home_view(request):
    if request.user.is_authenticated:
        # universities = University.objects.all()
        # for uni in universities:
        #     print(uni.name)
        #     if uni.name == request.user.university:n
        #         print(123)
        # notes = NotesUpload.objects.get(university__exact = request.user.university)   
        notes = NotesUpload.objects.all()           
        context = {
            'notes': notes,
        }
        return render(request, "notes.html", context)
    else:
        return redirect('/')
    return render(request, "notes.html")