from django.urls import path
from .views import *

urlpatterns = [
    path('', Login.as_view(), name='Login'),
    path('Stats_HTML/', Stats_HTML, name='Stats_HTML'),
    # path('cool_HTML/', cool_HTML, name='cool_HTML'),
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
]
