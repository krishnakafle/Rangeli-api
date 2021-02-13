from django.urls import path
from dataAPI import views

urlpatterns = [
    path('dashboard-data/', views.dashboardDataList.as_view(), name='dashboard'),
    path('household/questions/', views.householdQuestionsList.as_view(), name='household-questions'),
    path('household/data/<str:variable>/<int:ward>/', views.householdQueryDataList.as_view(), name='household-data'),
    path('household/micro-data/<str:variable>/<str:variableValue>/<int:ward>/', views.householdMicroDataList.as_view(), name='household-micro-data'),
    path('personal/questions/', views.personalQuestionsList.as_view(), name='personal-questions'),
    path('personal/data/<str:variable>/<int:ward>/', views.personalQueryDataList.as_view(), name='personal-data'),
    path('personal/micro-data/<str:variable>/<str:variableValue>/<int:ward>/', views.personalMicroDataList.as_view(), name='personal-micro-data'),
    path('personal/data/all/', views.personalDataList.as_view(), name='personal-data-all'),

    # file download urls
    path('reports/download/<str:name>', views.FileDownloadListAPIView.as_view(), name='report-download')
]
