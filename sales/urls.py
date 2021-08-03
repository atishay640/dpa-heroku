from os import name
from django.urls import path, include
from sales.views import (DashboardView, getDashboardChartView, mediaDownloadView,)


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='sales_dashboard'),
    path('dashboard/data/', getDashboardChartView, name='dashboard_data'),
    path('media/download/<str:token>', mediaDownloadView, name='media_download'),
    path('api/', include('sales.api.urls')),
]   

