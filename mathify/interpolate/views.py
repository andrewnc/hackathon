from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import NameForm
# Create your views here.

def index(request):
	return render(request, 'app/index.html')

def drawT(shift=None):
	#TODO: Handle proper Shifting for characters
	coords = [["237","620","237","620","237","120","237","120"],["237","120","237","35","226","24","143","19"],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	li = []
	for a in coords:
		if len(a) == 8:
			li.append("\\left(\\left(" + a[0] + "\\left(1-t\\right)^3+3*" + a[1] + "\\left(1-t\\right)^2t+3*" + a[2] + "\\left(1-t\\right)t^2+" + a[3] + "t^3\\right),\\ " + a[4] + "\\left(1-t\\right)^3+3*" + a[5] + "\\left(1-t\\right)^2t+3*" + a[6] + "\\left(1-t\\right)t^2+" + a[7] + "t^3\\right)")
		else:
			continue
	return li

def drawChar(c):
	if c == 'T':
		print "Calling drawT"
		return drawT()
	else:
		return "None"

def prepareLatex(text):
	"""Take the text and prepare it to be graphed in a Latex format.
		Parameters:
		text (str): The text we are wanting to graph. V.0 only allows basic characters
		Returns:
		letters (list): Each letter is an element of the list returned by this function."""
	letters = []
	for c in text:
		print "attempting to draw",c
		letters.append(drawChar(c))
	return letters


def getFormData(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

    text = form['text_input'].value()

    letters = prepareLatex(text)
    #print(latexs[0][0])
    #print(latexs[0][1])
    return render(request, 'app/name.html', {'text': text, 'letters': letters})
