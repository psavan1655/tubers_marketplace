from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber

# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    team = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_youtubers = Youtuber.objects.order_by('-created_date')

    data = {
        'sliders': sliders,
        'team': team,
        'featured_youtubers': featured_youtubers,
        'all_youtubers': all_youtubers,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    team = Team.objects.all()
    data = {
        'team': team,
    }
    return render(request, 'webpages/about.html', data)

def services(request):
    return render(request, 'webpages/services.html')
    
def contact(request):
    return render(request, 'webpages/contact.html')