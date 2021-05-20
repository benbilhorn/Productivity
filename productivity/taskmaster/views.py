from django.shortcuts import render
from django.http import HttpResponse
from taskmaster.models import Inbox
from django.db.models import Count

# Create your views here.


def home(request):
    inboxdata = Inbox.objects.all()
    numberofinboxtasks = Inbox.objects.aggregate(totalinboxtasks=Count('inboxTaskName'))
    context = {
        'numberofinboxtasks': numberofinboxtasks,
        'inboxdata': inboxdata}
    return render(request, 'taskmaster/home.html', context)


def saveinbox(request):
    if 'taskname' in request.GET:
        taskname = request.GET.get('taskname')
        if Inbox.objects.filter(inboxTaskName=taskname).exists():
            print("Entry contained in queryset")
        else:
            inboxobj = Inbox(inboxTaskName=taskname)
            inboxobj.save()
    return HttpResponse('Success')


def sortinbox(request):
    if 'inboxid' and 'taskorproject' in request.GET:
        inboxid = request.GET.get('inboxid')
        taskorproject = request.GET.get('taskorproject')

    return HttpResponse('Success')
