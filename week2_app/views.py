from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from .models import Subscription, Subscriber
from .forms import SubscriberForm

def get_subscriber(request):
    if(request.method == "POST"):
        form = SubscriberForm(request.POST)
        subscription = get_object_or_404(Subscription, pk="test")

        if form.is_valid():
            try:
                new_subscriber = subscription.subscriber_set.create(email=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'] )
            except (KeyError, Subscriber.DoesNotExist):
                return render(request, "index.html", {'form': form})
                
            new_subscriber.save()
            return HttpResponseRedirect('/')

    else:
        form = SubscriberForm()
    
    return render(request, "index.html", {'form': form})

def char_count(request):
    text = request.GET.get("text", "")

    return JsonResponse({"count": len(text)})

def index(request):
    return render(request, 'index.html')