from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic import DetailView
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

def reference_api(request):
    """ Reference model verisini json olarak gönderir."""
    data2 = ReferenceServiceAnalytic.objects.all().values()
    return JsonResponse(list(data2), safe=False)


def reference_chart(request):
    """ Burada d3.js ile oluşturulan görseller yer alıyor. """
    return render(request, 'cockpit/reference_chart.html', locals())

def index(request):
    """ 
    ReferenceServiceAnalytic modelinin index sayfası.
    """
    latest_data_list = ReferenceServiceAnalytic.objects.order_by('-record_date')
    data = serialize('json', ReferenceServiceAnalytic.objects.all())
    context = { 'latest_data_list'  : latest_data_list,
                'modul_baslik'      :"Referans Hizmetleri Analitikleri",
                'data'              : data}
    return render(request, 'cockpit/index.html', context)

""" def detail(request, analytic_id):
    return HttpResponse("You're on the analytics detail page %s." % analytic_id)

def new_record_ref(request):
    form = ReferenceAnalyticForm()
    return render(request, 'cockpit/new_record_ref.html', locals()) """


class MarketingPage(View):
    """
    Web sitesine açılışta görünecek olan ilk sayfayı yüklemek ile sorumludur.
    """
    baslik = "Hoşgeldiniz"
    

    def get(self, request):
        return render(request, 'cockpit/marketing.html', locals())


class RefAnalyticsFormView(View):
    """
    ReferenceServiceAnalytic modeli için;
    GET, POST, PUT, DELETE görevlerini yerine getirir.
    """
    form = ReferenceAnalyticForm()
    template_name = 'cockpit/new_record_ref.html'
    
    obj = ReferenceServiceAnalytic()

    def get(self, request, *args, **kwargs):
        """
        url : 'referans/yeni/'
        url : 'referans/<int:pk>/duzenle/
        Bu fonksiyona hem düzenleme hemde yeni veri sayfası görüntüleme isteği gelebilir.
        Eğer düzenleme sayfası isteği varsa pk dolu olmalıdır.
        Aksi halde yeni gönderi sayfası talep edildiği anlaşılacaktır.
        """
        pk = self.kwargs.get('pk')
        # silme işlemi
        if(request.GET.get('sil')):
            try:
                self.obj  =  ReferenceServiceAnalytic.objects.get(pk=pk)
                self.obj.delete()
                return redirect('reference_index')
            except:
                return HttpResponse("Böyle bir sayfa yok")
            return HttpResponse("silinecek veri id'si {}".format(str(pk)))

        # düzenleme işlemi
        if pk:
            try:
                self.obj = ReferenceServiceAnalytic.objects.get(pk=pk)
                initial = { 'user_from_out' : self.obj.user_from_out,
                            'user_from_inside' :self.obj.user_from_inside,
                            'online_user_outside': self.obj.online_user_outside,
                            'online_user_inside': self.obj.online_user_inside,
                            'borrowed_books': self.obj.borrowed_books,
                            'retired_books': self.obj.retired_books,
                            'photocopy': self.obj.photocopy,
                            'record_date': self.obj.record_date}
                form = ReferenceAnalyticForm(initial = initial)
                return render(request, self.template_name, {'form': form})
            except:
                return HttpResponse("Böyle bir sayfa yok")

            print("NESNEYİ BUL VE FORMA BAS")
            print("PK var {}".format(str(pk)))
        else:
            form = self.form
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Bu fonksiyona hem düzenleme hem de yeni veri kaydetme isteği gelebilir.
        Eğer düzenleme isteği varsa pk dolu olmalıdır.
        Aksi halde yeni gönderi olduğu anlaşılacaktır.
        """
        pk = self.kwargs.get('pk')
        form = ReferenceAnalyticForm(request.POST)
        form_errors = []
        model_data = ReferenceServiceAnalytic()

        # eğer düzenleme isteği gelirse düzenlenecek nesneyi bul
        if pk:
            try:
                model_data = ReferenceServiceAnalytic.objects.get(pk=pk)
            except:
                return HttpResponse("Böyle bir düzenlenme isteği uygun değil")
        
        # normal isteklerde burada devam et
        # form geçerliyse bu işlemleri yap
        if form.is_valid():
            model_data.user_from_out = request.POST.get('user_from_out')
            model_data.user_from_inside = request.POST.get('user_from_inside')
            model_data.online_user_outside = request.POST.get('online_user_outside')
            model_data.online_user_inside = request.POST.get('online_user_inside')
            model_data.borrowed_books = request.POST.get('borrowed_books')
            model_data.retired_books = request.POST.get('retired_books')
            model_data.photocopy = request.POST.get('photocopy')
            model_data.record_date = request.POST.get('record_date')
        
        # forma eksi değer girilemez kontrol
            if model_data.is_minus_value_entered():
                form_errors.append("Forma eksi (-) değer girilemez.")
                return render(request, self.template_name, {'form': form, 'errors' : form_errors})
            else:
                model_data.save()
                return redirect('detail', pk= model_data.pk)
        return render(request, self.template_name, {'form': form})

class RefAnalyticsDetailView(DetailView):
    """
    ReferenceServiceAnalytic modeli için ayrıntılar sayfası oluşturur.
    """
    model = ReferenceServiceAnalytic