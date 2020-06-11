from django.shortcuts import render
from django.http import HttpResponse
from .models import ReferenceServiceAnalytic
# Create your views here.

def index(request):
    latest_data_list = ReferenceServiceAnalytic.objects.order_by('-record_date')[:5]
    context = {'latest_data_list': latest_data_list}
    return render(request, 'cockpit/index.html', context)

def detail(request, analytic_id):
    return HttpResponse("You're on the analytics detail page %s." % analytic_id)

def new_record_ref(request):
    
    return render(request, 'cockpit/new_record_ref.html', locals())