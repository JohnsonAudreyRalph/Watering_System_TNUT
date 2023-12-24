from django.urls import path
from .views import *

urlpatterns = [
    path('', Login.as_view(), name='Login'),
    path('Stats_HTML/', Stats_HTML, name='Stats_HTML'),
    path('info_HTML/', info_HTML, name='info_HTML'),
    path('home_HTML/', home_HTML, name='home_HTML'),
    path('daily_HTML/', daily_HTML, name='daily_HTML'),
    path('pump_HTML/', pump_HTML, name='pump_HTML'),
    path('user_HTML/', user_HTML, name='user_HTML'),
    path('manager_Delete/<int:id>/', manager_Delete, name='manager_Delete'),
    path('manager_Update/<str:id>', manager_Update, name='manager_Update'),
    path('location_HTML/', location_HTML, name='location_HTML'),
    path('logout/', Logout, name='logout'),
    path('Show_HaoDat_info', Show_HaoDat_info, name='Show_HaoDat_info'),
    path('Show_HaoDat_stats', Show_HaoDat_stats, name='Show_HaoDat_stats'),
    path('Show_ThaiMinh_info', Show_ThaiMinh_info, name='Show_ThaiMinh_info'),
    path('Show_ThaiMinh_status', Show_ThaiMinh_status, name='Show_ThaiMinh_status'),
    path('Show_KheCoc_info', Show_KheCoc_info, name='Show_KheCoc_info'),
    path('Show_KheCoc_status', Show_KheCoc_status, name='Show_KheCoc_status'),
    # ======================================================
    path('Show_API_HaoDat', Show_API_HaoDat, name='Show_API_HaoDat'),
    # path('Create_API_HaoDat', Create_API_HaoDat, name='Create_API_HaoDat'),
    path('Update_API_Hao_Dat', Update_API_Hao_Dat, name='Update_API_Hao_Dat'),

    path('Show_API_KheCoc', Show_API_KheCoc, name='Show_API_KheCoc'),
    # path('Create_API_KheCoc', Create_API_KheCoc, name='Create_API_KheCoc'),
    path('Update_API_KheCoc', Update_API_KheCoc, name='Update_API_KheCoc'),

    path('Show_API_ThaiMinh', Show_API_ThaiMinh, name='Show_API_ThaiMinh'),
    # path('Create_API_ThaiMinh', Create_API_ThaiMinh, name='Create_API_ThaiMinh'),
    path('Update_API_ThaiMinh', Update_API_ThaiMinh, name='Update_API_ThaiMinh')
]
