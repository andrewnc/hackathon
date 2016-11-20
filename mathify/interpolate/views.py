from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import NameForm
import math_letters as draw
# Create your views here.

def index(request):
	letters = prepareLatex("Mathify")
	return render(request, 'app/index.html', {'letters': letters})

def landing_render(request):
	return render(request, 'app/landing.html')

def prepareLatex(text, sillify=False, scribble=False):
	"""Take the text and prepare it to be graphed in a Latex format.
		Parameters:
		text (str): The text we are wanting to graph. V.0 only allows basic characters
		Returns:
		letters (list): Each letter is an element of the list returned by this function."""
	letters = []
	x_shift = 0
	y_shift = 0 #TODO: Handle long sentences with wrapping somehow.
	for c in text:
		if c == 'g' or c == 'G' or c == 's' or c == 'S':
			character, discard, discard = draw.char(c, x_shift, 0, scribble=scribble)
			letters.append(character)
			character, x_shift, y_shift = draw.char(c+c, x_shift, 0, scribble=scribble)
		else:
			character, x_shift, y_shift = draw.char(c, x_shift, 0, sillify, scribble)
		x_shift += 25 #add a bit of a buffer between characters.
		letters.append(character)
	return letters


def getFormData(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

    text = form['text_input'].value()
    sillify = form['silly'].value()
    scribble = form['scribble'].value()

    letters = prepareLatex(text, sillify, scribble)

    return render(request, 'app/name.html', {'text': text, 'letters': letters})
