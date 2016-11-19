from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import NameForm
# Create your views here.

def index(request):
	return render(request, 'app/index.html')



def getFormData(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

    text = form['text_input'].value()

    return render(request, 'app/name.html', {'text': text})
