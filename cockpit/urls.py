from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:analytic_id>/', views.detail, name="detail"),
    path('new_record_ref', views.new_record_ref, name='new_record_ref')
]