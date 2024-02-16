from django.shortcuts import render
from .models import RenewablePowerGeneration, Article, Subscriber
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def energy_data(request):
    data = RenewablePowerGeneration.objects.all()
    return render(request, 'core/energy_data.html', {'data': data})

def energy_data(request):
    sort_order = request.GET.get('sort_order', 'default')

    if sort_order == 'lowest_to_highest':
        data = RenewablePowerGeneration.objects.order_by('contribution_twh')
    elif sort_order == 'highest_to_lowest':
        data = RenewablePowerGeneration.objects.order_by('-contribution_twh')
    else:
        data = RenewablePowerGeneration.objects.all()

    context = {
        'data': data,
        'sort_order': sort_order
    }

    return render(request, 'core/energy_data.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def latest(request):
    return render(request, 'core/latest.html')

def latest(request):
    articles = Article.objects.all()
    return render(request, 'latest.html', {'articles': articles})


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        existing_subscriber = Subscriber.objects.filter(email=email).exists()
        if existing_subscriber:
            return render(request, 'subscribe_error.html', {'email': email})
        else:
            Subscriber.objects.create(email=email)
            return HttpResponseRedirect(reverse('subscribe_success'))
    else:
        return render(request, 'core/subscribe.html')
    
def subscribe_success(request):
    return render(request, 'core/subscribe_success.html')