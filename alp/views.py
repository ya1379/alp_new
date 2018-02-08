from django.template.loader import get_template
from django.template import loader
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
import datetime
def index(request):
 now = datetime.datetime.now()
 t = get_template('index.html')
 context = {'current_date': now}
 #html = t.render(Context({'current_date': now}))
 return HttpResponse(t.render(context, request))