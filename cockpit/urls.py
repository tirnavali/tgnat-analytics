from django.urls import path
from . import views

urlpatterns = [
    path('selamla/', views.GreetingView.as_view()),
    path('', views.MarketingPage.as_view(), name='marketing_page'),

    path('referans/', views.index, name='referance'),        
    path('referans/yeni/', views.RefAnalyticsFormView.as_view(), name='new_record_ref'),
    path('referans/<int:pk>/', views.RefAnalyticsDetailView.as_view(), name="detail"),
    path('referans/<int:pk>/duzenle/', views.RefAnalyticsFormView.as_view(), name='edit-reference')
]

