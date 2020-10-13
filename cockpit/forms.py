from django import forms
from .models import *
from django.utils import timezone

# class ReferenceAnalyticForm(forms.Form):
#     user_from_out = forms.IntegerField(label="Dışarıdan gelen kullanıcı sayısı")
#     user_from_inside = forms.IntegerField(label="Kurum içi gelen kullanıcı sayısı")

#     online_user_outside = forms.IntegerField(label="Online gelen dış kullanıcı sayısı")
#     online_user_inside = forms.IntegerField(label="Online gelen iç kullanıcı sayısı")

#     borrowed_books = forms.IntegerField(label="Ödünç verilen kitap sayısı")
#     retired_books = forms.IntegerField(label="İade edilen kitap sayısı")

#     photocopy = forms.IntegerField(label="Çekilen fotokopi sayısı")
#     record_date = forms.DateTimeField(label="Verilerin toplandığı tarih(ay)", 
#         widget=forms.TextInput(attrs={'placeholder':'2019-01-30'}))

class SaglamaAnalyticForm(forms.Form):

    pub_type              = forms.ModelChoiceField(queryset = PubType.objects, label='Yayın türü:')
    #report                = forms.IntegerField(disabled = True)
    pub_arrived_as_supply = forms.IntegerField(initial = 0, label='Derlemeden gelen yayın sayısı:', max_value=100000, min_value=0)
    pub_arrived_as_gift   = forms.IntegerField(initial = 0, label='Hediye gelen yayın sayısı:' , max_value=100000, min_value=0)
    pub_bought            = forms.IntegerField(initial = 0, label='Satın alınan yayın sayısı:' , max_value=100000, min_value=0)
    pub_saved_as_supply   = forms.IntegerField(initial = 0, label='Derlemeden koleksiyona alınan yayın sayısı:' , max_value=100000, min_value=0)
    pub_saved_as_gift     = forms.IntegerField(initial = 0, label='Hediyelerden koleksiyona alınan yayın sayısı:'  , max_value=100000, min_value=0)
    pub_saved_as_old      = forms.IntegerField(initial = 0, label='Eski etiketiyle koleksiyona alınan yayın sayısı:'  , max_value=100000, min_value=0)


    def save_form(self, report_id):
        ''' Saves form data to model'''
        acquisition_analytic = AcquisitionAnalytic()

        print("Baskı alınıyor : \t" + str(self.fields.values()))
        print("Baskı alınıyor : \t" + str(self.fields['pub_type']))
        print("Baskı alınıyor : \t" + str(self.fields['pub_arrived_as_supply']))

        if self.is_valid():
            # is_valid çağırıldıktan sonra cleaned_data sözlüğünden verileri alabiliriz.
            print("Her şey yolunda baskıya hazırım ######### \n \n")
            print("CLeaned data : " + str(self.cleaned_data))


            acquisition_analytic.pub_type = self.cleaned_data["pub_type"]
            acquisition_analytic.report                = AcquisitionReport.objects.get(pk = int(report_id))
            acquisition_analytic.pub_arrived_as_supply = self.cleaned_data['pub_arrived_as_supply']
            acquisition_analytic.pub_arrived_as_gift   = self.cleaned_data['pub_arrived_as_gift']
            acquisition_analytic.pub_bought            = self.cleaned_data['pub_bought']
            acquisition_analytic.pub_saved_as_supply   = self.cleaned_data['pub_saved_as_supply']
            acquisition_analytic.pub_saved_as_gift     = self.cleaned_data['pub_saved_as_gift']
            acquisition_analytic.pub_saved_as_old      = self.cleaned_data['pub_saved_as_old']

            acquisition_analytic.save()
        else:
            return self.errors
        

        


    #report_date           = forms.DateField(initial = timezone.now())

class SaglamaReportForm(forms.ModelForm):
    class Meta:
        model = AcquisitionReport
        fields = '__all__'
   
        widgets = {
                        
            'date' : forms.DateInput(attrs={ 'class' : 'form-control' ,
                                              'placeholder':'2019-01-30'}),
        #     'notes' : forms.Textarea(attrs={ 'class' : 'form-control',
        #     'cols': 80, 'rows': 3}),
         }


class SaglamaForm(forms.ModelForm):
    class Meta:
        model = AcquisitionAnalytic
        fields = '__all__'
   
        widgets = {
                        
            'date' : forms.DateInput(attrs={ 'class' : 'form-control' ,
                                             'placeholder':'2019-01-30'}),
            'notes' : forms.Textarea(attrs={ 'class' : 'form-control',
            'cols': 80, 'rows': 3}),
        }


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = ReferenceServiceAnalytic
        fields = '__all__'
   
        widgets = {
                        
            'date' : forms.DateInput(attrs={ 'class' : 'form-control' ,
                                             'placeholder':'2019-01-30'}),
            'notes' : forms.Textarea(attrs={ 'class' : 'form-control',
            'cols': 80, 'rows': 3}),
        }
