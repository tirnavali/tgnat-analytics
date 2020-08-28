from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home_page, name='home_page'),
    path('referans/', views.index, name='reference_index'),        
    path('referans/yeni/', views.RefAnalyticsFormView.as_view(), name='new_record_ref'),
    path('referans/<int:pk>/', views.RefAnalyticsDetailView.as_view(), name="detail"),
    path('referans/<int:pk>/duzenle/', views.RefAnalyticsFormView.as_view(), name='edit_reference'),
    path('referans/chart', views.reference_chart, name="reference_chart"),
    path('referans/line_chart', views.reference_line_chart, name='reference_line_chart'),
    path('api/referans/', views.reference_api, name="reference-api"),

    path('saglama/', views.acquisition_report_index, name='acquisition_report_index'),
    path('saglama/yeni', views.new_acquisition_report, name='new_acquisition_report'),
    path('saglama/yeni-2', views.SaglamaAnalyticFormView.as_view(), name='saglama_yeni_2'),

]
