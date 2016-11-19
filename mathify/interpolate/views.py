from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import NameForm
import math_letters as draw
# Create your views here.

def index(request):
	return render(request, 'app/index.html')

def landing_render(request):
	return render(request, 'app/landing.html')

def drawChar(c, x_shift, y_shift=0):
	"""NOTE: When building characters make sure that the coordinates are set up
	to have [x1,y1,x2,y2,x3,y3,x4,y4]
	Parameters:
	c (str): The character to be drawn
	x_shift (int): the amount of horizontal shift needed.
	y_shift (int): The amount of vertical shift needed.
	"""
	if c == 'T':
		return draw.T(x_shift, y_shift)
	else:
		return "None"

def prepareLatex(text):
	"""Take the text and prepare it to be graphed in a Latex format.
		Parameters:
		text (str): The text we are wanting to graph. V.0 only allows basic characters
		Returns:
		letters (list): Each letter is an element of the list returned by this function."""
	letters = []
	x_shift = 0
	y_shift = 0 #TODO: Handle long sentences with wrapping somehow.
	for c in text:
		character, x_shift = drawChar(c, x_shift, y_shift)
		x_shift += 25 #add a bit of a buffer between characters.
		letters.append(character)
	return letters


def getFormData(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

    text = form['text_input'].value()

    letters = prepareLatex(text)
    #print(latexs[0][0])
    #print(latexs[0][1])
    return render(request, 'app/name.html', {'text': text, 'letters': letters})
