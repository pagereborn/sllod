from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from sllod.models import Poll, Option, OptionVote
from sllod.forms import PollForm
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django import forms
from django.utils import timezone
from django.utils import simplejson
from django.db import IntegrityError
from django.db.models import Avg,Sum
from django.views.generic.detail import BaseDetailView, \
    SingleObjectTemplateResponseMixin
# Create your views here.

def index(request):
    latest_poll_list = Poll.objects.order_by('-created_at')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_option = p.option_set.get(pk=request.POST['option'])
        
    except (KeyError, Option.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_option.votes += 1
        selected_option.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
                                    
def add_poll(request):
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            
            model_instance = form.save(commit=False)
            model_instance.created_by = request.user
            model_instance.timestamp = timezone.now()
            
            model_instance.save()
    else:
        form = PollForm()
        
    latest_poll_list = Poll.objects.order_by('-created_at')[:5]
    #poll_list_options = latest_poll_list.
    return render(request, "polls/create_poll.html", {'form': form, 'latest_poll_list': latest_poll_list})

def create_poll(request):
    latest_poll_list = Poll.objects.order_by('-created_at')[:15]
    if request.POST:
        form = PollForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            
            model_instance = form.save(commit=False)
            model_instance.created_by = request.user
            model_instance.timestamp = timezone.now()
            
            model_instance.save()
            if request.is_ajax():
                return render(request, "polls/poll_list.html", {'latest_poll_list': latest_poll_list})
    else:
        form = PollForm()
        
    
    #poll_list_options = latest_poll_list.
    return render(request, "polls/create_poll.html", {'form': form, 'latest_poll_list': latest_poll_list})
def ajax_poll_list(request):
    latest_poll_list = Poll.objects.order_by('-created_at')[:15]
    return render(request, "polls/poll_list.html", {'latest_poll_list': latest_poll_list})

def option_vote(request):
    if request.POST:
        p = get_object_or_404(Poll, pk=request.POST['poll'])
        o = get_object_or_404(Option, pk=request.POST['option'])
        
        
        votes = o.votes
        try:
            ov = OptionVote(poll = p, option = o, created_by = request.user, has_changed = False, created_at = timezone.now());
            ov.save()
            votes = votes + 1
            o.votes = votes
            o.save()
            all_options = Option.objects.filter(poll_id = request.POST['poll'])
            total_votes = all_options.aggregate(Sum('votes'))['votes__sum']
            p.share = 100/total_votes
            #p.share = 33.00
            p.save()
            for opt in all_options:
                opt.percentage = p.share * opt.votes
                opt.save()
            
            
            
        except IntegrityError as e:
            return HttpResponse(votes)

    return HttpResponse(votes)