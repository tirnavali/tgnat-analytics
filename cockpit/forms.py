from django import forms

class ReferenceAnalyticForm(forms.Form):
    user_from_out = forms.IntegerField(label="Dışarıdan gelen kullanıcı sayısı")
    user_from_inside = forms.IntegerField(label="Kurum içi gelen kullanıcı sayısı")

    online_user_outside = forms.IntegerField(label="Online gelen dış kullanıcı sayısı")
    online_user_inside = forms.IntegerField(label="Online gelen iç kullanıcı sayısı")

    borrowed_books = forms.IntegerField(label="Ödünç verilen kitap sayısı")
    retired_books = forms.IntegerField(label="İade edilen kitap sayısı")

    photocopy = forms.IntegerField(label="Çekilen fotokopi sayısı")
    record_date = forms.DateTimeField(label="Verilerin toplandığı tarih(ay)", 
        widget=forms.TextInput(attrs={'placeholder':'2019-01-30'}))