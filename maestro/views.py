from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import *
from .forms import *


# Create your views here.

def index(request):
    latest_channel_list = Channel.objects.order_by('number')
    context = {'latest_channel_list': latest_channel_list}
    return render(request, 'maestro/index.html', context)

def newchannel(request):
    return detail(request, None)
    
def deletechannel(request, channel_id):
    channel = get_object_or_404(Channel, pk=channel_id)
    channel.delete()
    return HttpResponseRedirect(reverse('maestro:index'))

def detail(request, channel_id):
    if (channel_id != None):
        channel = get_object_or_404(Channel, pk=channel_id)
    if request.method == 'POST':
        form = AddChannel(request.POST)
        if form.is_valid():
            if (channel_id != None):
                channel.delete()
            else:
                if Channel.objects.filter(number=form.cleaned_data['number']).exists():
                    latest_channel_list = Channel.objects.order_by('number')
                    context = {'latest_channel_list': latest_channel_list, "error_message": "Channel already in use"}
                    return render(request, 'maestro/index.html', context)
            newChannel = Channel(name = form.cleaned_data['name'])
            newChannel.number = form.cleaned_data['number']
            newChannel.rangeMin = form.cleaned_data['rangeMin']
            newChannel.rangeMax = form.cleaned_data['rangeMax']
            newChannel.target = form.cleaned_data['target']
            newChannel.speed = form.cleaned_data['speed']
            newChannel.acceleration = form.cleaned_data['acceleration']
            newChannel.save()
            
            return HttpResponseRedirect(reverse('maestro:index'))
        else:
            latest_channel_list = Channel.objects.order_by('number')
            context = {'latest_channel_list': latest_channel_list, "error_message": "Invalid data"}
            return render(request, 'maestro/index.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
            if (channel_id != None):
                form = AddChannel(instance=channel)
                return render(request, 'maestro/newchannel.html', {'form': form, 'old': channel_id})
            else:
                form = AddChannel()
                return render(request, 'maestro/newchannel.html', {'form': form})


