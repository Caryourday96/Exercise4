
# Create your views here.
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm


#def index(request):
 #   return HttpResponse("Hello, world. You're at Kayode's Notes Webpage .")

def index(request):
    notes = Note.objects
    template = loader.get_template('note.html')
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    context = {'notes': notes, 'form': form}
    return render(request, 'note.html', context)
    # return render_to_response("note.html", notes)

#The View.py file is edited to link to the template
#Author Kayode Adetunji


# Create your views here.

