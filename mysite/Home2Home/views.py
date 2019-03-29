# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.views.generic import UpdateView, ListView
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse
from Home2Home.models import thing_list, persons
# Create your views here.
class home(ListView):
	model = persons
	context_object_name = 'persons'
	template_name = 'home.html'

def showItems(request,id):
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


def delete_task(request, id):
	task = get_object_or_404(thing_list, pk=id)
	task.delete()
	redir_url = reverse(
		"showItems",
		kwargs={"id": task.person.pk},
	)

	messages.success(request, "Task '{}' has been deleted".format(task.title))
	return redirect(redir_url)





