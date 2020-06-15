from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('selamla/', views.GreetingView.as_view()),
    path('<int:analytic_id>/', views.detail, name="detail"),
    path('new_record_ref/', views.RefAnalyticsFormView.as_view(), name='new_record_ref')
]