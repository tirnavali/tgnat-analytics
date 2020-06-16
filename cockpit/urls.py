from django.urls import path
from . import views

urlpatterns = [
    path('', views.MarketingPage.as_view(), name='marketing_page'),
    path('referans/', views.index, name='referance'),
    path('selamla/', views.GreetingView.as_view()),
    path('<int:analytic_id>/', views.detail, name="detail"),
    path('referans/yeni/', views.RefAnalyticsFormView.as_view(), name='new_record_ref'),
    path('referans/<int:analytic_id>', views.detail, name="detail")
]