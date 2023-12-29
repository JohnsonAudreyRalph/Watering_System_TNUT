from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    path('Show_API_HaoDat_read', Show_API_HaoDat_read, name='Show_API_HaoDat_read'),
    # path('Create_API_HaoDat_read', Create_API_HaoDat_read, name='Create_API_HaoDat_read'),
    path('Update_API_Hao_Dat_read', Update_API_Hao_Dat_read, name='Update_API_Hao_Dat_read'),
    path('Show_API_HaoDat_R_W', Show_API_HaoDat_R_W, name='Show_API_HaoDat_R_W'),
    # path('Create_API_HaoDat_R_W', Create_API_HaoDat_R_W, name='Create_API_HaoDat_R_W'),
    path('Update_API_Hao_Dat_R_W', Update_API_Hao_Dat_R_W, name='Update_API_Hao_Dat_R_W'),
    path('Show_API_KheCoc_read', Show_API_KheCoc_read, name='Show_API_KheCoc_read'),
    # path('Create_API_KheCoc_read', Create_API_KheCoc_read, name='Create_API_KheCoc_read'),
    path('Update_API_KheCoc_read', Update_API_KheCoc_read, name='Update_API_KheCoc_read'),
    path('Show_API_KheCoc_R_W', Show_API_KheCoc_R_W, name='Show_API_KheCoc_R_W'),
    # path('Create_API_KheCoc_R_W', Create_API_KheCoc_R_W, name='Create_API_KheCoc_R_W'),
    path('Update_API_KheCoc_R_W', Update_API_KheCoc_R_W, name='Update_API_KheCoc_R_W'),
    path('Show_API_ThaiMinh_read', Show_API_ThaiMinh_read, name='Show_API_ThaiMinh_read'),
    # path('Create_API_ThaiMinh_read', Create_API_ThaiMinh_read, name='Create_API_ThaiMinh_read'),
    path('Update_API_ThaiMinh_read', Update_API_ThaiMinh_read, name='Update_API_ThaiMinh_read'),
    path('Show_API_ThaiMinh_R_W', Show_API_ThaiMinh_R_W, name='Show_API_ThaiMinh_R_W'),
    # path('Create_API_ThaiMinh_R_W', Create_API_ThaiMinh_R_W, name='Create_API_ThaiMinh_R_W'),
    path('Update_API_ThaiMinh_R_W', Update_API_ThaiMinh_R_W, name='Update_API_ThaiMinh_R_W'),
    
]

urlpatterns += staticfiles_urlpatterns()