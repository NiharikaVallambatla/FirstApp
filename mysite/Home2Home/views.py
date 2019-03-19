# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import UpdateView, ListView
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from Home2Home.models import thing_list, persons
# Create your views here.
class home(ListView):
	model = persons
	context_object_name = 'persons'
	template_name = 'home.html'

def showItems1(request,id):
	print(request,str(id))
	if (request.POST.get('from')):
		print("from")
		thing_list.objects.create(
			title=request.POST.get('from'),
			person=persons(id),
			fromHome=1
		)
	if (request.POST.get('to')):
		print("to")
		thing_list.objects.create(
			title=request.POST.get('to'),
			person=persons(id),
			fromHome=0
		)
	for row in thing_list.objects.all():
		if thing_list.objects.filter(Q(title=row.title) & Q(person=(row.person))).count() > 1:
			row.delete()
	person_name=persons.objects.get(id=int(id))
	items = thing_list.objects.filter(person=int(id))
	return render(request,'listing.html',{"name":person_name,"data":items})




