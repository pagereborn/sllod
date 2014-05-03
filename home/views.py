from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from sllod.forms import PollForm
from sllod.models import Poll, Option, OptionVote
from django.utils import timezone
from django.db import IntegrityError
def index(request):
    latest_poll_list = Poll.objects.order_by('-created_at')[:15]
    if request.POST:
        form = PollForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            
            model_instance = form.save(commit=False)
            model_instance.created_by = request.user
            model_instance.created_at = timezone.now()
            model_instance.save()
            if request.is_ajax():
                return render(request, "polls/poll_list.html", {'latest_poll_list': latest_poll_list})
    else:
        form = PollForm()
        
    return render(request, "home/index.html", {'form': form, 'latest_poll_list': latest_poll_list})
    #return render(request, 'home/index.html')