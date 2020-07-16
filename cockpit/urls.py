from django.urls import path
from . import views

urlpatterns = [    
    path('', views.MarketingPage.as_view(), name='marketing_page'),
    path('referans/', views.index, name='reference_index'),        
    path('referans/yeni/', views.RefAnalyticsFormView.as_view(), name='new_record_ref'),
    path('referans/<int:pk>/', views.RefAnalyticsDetailView.as_view(), name="detail"),
    path('referans/<int:pk>/duzenle/', views.RefAnalyticsFormView.as_view(), name='edit_reference'),
    path('referans/chart', views.reference_chart, name="reference-chart"),
    path('api/referans/', views.reference_api, name="reference-api")
]

