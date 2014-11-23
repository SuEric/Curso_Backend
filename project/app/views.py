from django.shortcuts import render_to_response
from datetime import datetime

# El shortcut render_to_response equivale a todo esto
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

# Create your views here.
def hora_actual(request):
	""" Modo sin shortcut
	ahora = datetime.now()
	t = get_template("hora.html")
	c = Context({"hora":ahora,"usuario":"Freddier"})
	html = t.render(c)
	return HttpResponse(html)
	"""
	# Modo con shortcut
	now = datetime.now()
	return render_to_response('hora.html', {'hora':now, 'usuario':'Freddier'})