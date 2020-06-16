from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import ReferenceServiceAnalytic
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group
from cockpit.forms import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def index(request):
    latest_data_list = ReferenceServiceAnalytic.objects.order_by('-record_date')
    context = {'latest_data_list': latest_data_list}
    return render(request, 'cockpit/index.html', context)

def detail(request, analytic_id):
    return HttpResponse("You're on the analytics detail page %s." % analytic_id)

def new_record_ref(request):
    form = ReferenceAnalyticForm()
    return render(request, 'cockpit/new_record_ref.html', locals())

class GreetingView(View):
    greeting = "Good day"

    def get(self, request):
        return HttpResponse(self.greeting)

class MarketingPage(View):
    baslik = "Hoşgeldiniz"

    def get(self, request):
        return render(request, 'cockpit/marketing.html', locals())


class RefAnalyticsFormView(View):
    form = ReferenceAnalyticForm()
    template_name = 'cockpit/new_record_ref.html'

    def get(self, request):
        form = self.form
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ReferenceAnalyticForm(request.POST)
        form_errors = []
        if form.is_valid():
    
            model_data = ReferenceServiceAnalytic()
            model_data.user_from_out = request.POST.get('user_from_out')
            model_data.user_from_inside = request.POST.get('user_from_inside')
            model_data.online_user_outside = request.POST.get('online_user_outside')
            model_data.online_user_inside = request.POST.get('online_user_inside')
            model_data.borrowed_books = request.POST.get('borrowed_books')
            model_data.retired_books = request.POST.get('retired_books')
            model_data.photocopy = request.POST.get('photocopy')
            model_data.record_date = request.POST.get('record_date')

            if model_data.is_minus_value_entered():
                form_errors.append("Forma eksi (-) değer girilemez.")
                return render(request, self.template_name, {'form': form, 'errors' : form_errors})
            else:
                model_data.save()
                return redirect('index')
        return render(request, self.template_name, {'form': form})