from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Manager_User, API_ThaiMinh_read, API_ThaiMinh_R_W, API_HaoDat_read, API_HaoDat_R_W, API_KheCoc_read, API_KheCoc_R_W

from rest_framework import status
from .serializers import Data_Serializer_HaoDat_R_W, Data_Serializer_HaoDat_read, Data_Serializer_KheCoc_R_W, Data_Serializer_KheCoc_read, Data_Serializer_ThaiMinh_R_W, Data_Serializer_ThaiMinh_read
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
from django.http import JsonResponse


# Create your views here.

@api_view(['GET'])
def Create_API_HaoDat_read(request):
    serializer = Data_Serializer_HaoDat_read(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Tạo mới API Hảo Đạt read thành công!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, tạo API thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def Show_API_HaoDat_read(request):
    data = API_HaoDat_read.objects.all()
    serializer = Data_Serializer_HaoDat_read(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def Update_API_Hao_Dat_read(request):
    data = get_object_or_404(API_HaoDat_read, pk=1)
    serializer = Data_Serializer_HaoDat_read(data, data=request.GET.dict())

    if serializer.is_valid():
        serializer.save()
        url = 'http://mrduck.id.vn/Show_API_HaoDat_read?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse({
                'message': json.dumps(response.json()) 
            }, status=status.HTTP_200_OK)

        return JsonResponse({'message': 'Cập nhật thành công!'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Lỗi, cập nhật không thành công!'}, status=status.HTTP_400_BAD_REQUEST)

# ===================================
@api_view(['GET'])
def Create_API_HaoDat_R_W(request):
    serializer = Data_Serializer_HaoDat_R_W(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Tạo mới API Hảo Đạt R & W thành công!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, tạo API thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def Show_API_HaoDat_R_W(request):
    data = API_HaoDat_R_W.objects.all()
    serializer = Data_Serializer_HaoDat_R_W(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def Update_API_Hao_Dat_R_W(request):
    data = get_object_or_404(API_HaoDat_R_W, pk=1)
    serializer = Data_Serializer_HaoDat_R_W(data, data=request.GET.dict())

    if serializer.is_valid():
        serializer.save()
        url = 'http://mrduck.id.vn/Show_API_HaoDat_R_W?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse({
                'message': json.dumps(response.json()) 
            }, status=status.HTTP_200_OK)

        return JsonResponse({'message': 'Cập nhật thành công!'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Lỗi, cập nhật không thành công!'}, status=status.HTTP_400_BAD_REQUEST)



# ===========================================================
@api_view(['GET'])
def Create_API_KheCoc_read(request):
    serializer = Data_Serializer_KheCoc_read(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Tạo mới API Khê Cốc read thành công!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, tạo API thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def Show_API_KheCoc_read(request):
    data = API_KheCoc_read.objects.all()
    serializer = Data_Serializer_KheCoc_read(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def Update_API_KheCoc_read(request):
    data = get_object_or_404(API_KheCoc_read, pk=1)
    serializer = Data_Serializer_KheCoc_read(data, data=request.GET.dict())

    if serializer.is_valid():
        serializer.save()
        url = 'http://mrduck.id.vn/Show_API_KheCoc_read?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse({
                'message': json.dumps(response.json()) 
            }, status=status.HTTP_200_OK)

        return JsonResponse({'message': 'Cập nhật thành công!'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Lỗi, cập nhật không thành công!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Create_API_KheCoc_R_W(request):
    serializer = Data_Serializer_KheCoc_R_W(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Tạo mới API Khê Cốc R & W thành công!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, tạo API thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def Show_API_KheCoc_R_W(request):
    data = API_KheCoc_R_W.objects.all()
    serializer = Data_Serializer_KheCoc_R_W(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def Update_API_KheCoc_R_W(request):
    data = get_object_or_404(API_KheCoc_R_W, pk=1)
    serializer = Data_Serializer_KheCoc_R_W(data, data=request.GET.dict())

    if serializer.is_valid():
        serializer.save()
        url = 'http://mrduck.id.vn/Show_API_KheCoc_R_W?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse({
                'message': json.dumps(response.json()) 
            }, status=status.HTTP_200_OK)

        return JsonResponse({'message': 'Cập nhật thành công!'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Lỗi, cập nhật không thành công!'}, status=status.HTTP_400_BAD_REQUEST)
# ===========================================================
@api_view(['GET'])
def Create_API_ThaiMinh_read(request):
    serializer = Data_Serializer_ThaiMinh_read(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Tạo mới API Thái Minh read thành công!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, tạo API thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def Show_API_ThaiMinh_read(request):
    data = API_ThaiMinh_read.objects.all()
    serializer = Data_Serializer_ThaiMinh_read(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def Update_API_ThaiMinh_read(request):
    data = get_object_or_404(API_ThaiMinh_read, pk=1)
    serializer = Data_Serializer_ThaiMinh_read(data, data=request.GET.dict())

    if serializer.is_valid():
        serializer.save()
        url = 'http://mrduck.id.vn/Show_API_ThaiMinh_read?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)

        return JsonResponse({'message': 'Cập nhật thành công!'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Lỗi, cập nhật không thành công!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Create_API_ThaiMinh_R_W(request):
    serializer = Data_Serializer_ThaiMinh_R_W(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Tạo mới API Thái Minh R & W thành công!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, tạo API thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def Show_API_ThaiMinh_R_W(request):
    data = API_ThaiMinh_R_W.objects.all()
    serializer = Data_Serializer_ThaiMinh_R_W(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def Update_API_ThaiMinh_R_W(request):
    data = get_object_or_404(API_ThaiMinh_R_W, pk=1)
    serializer = Data_Serializer_ThaiMinh_R_W(data, data=request.GET.dict())

    if serializer.is_valid():
        serializer.save()
        url = 'http://mrduck.id.vn/Show_API_ThaiMinh_R_W?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse({
                'message': json.dumps(response.json()) 
            }, status=status.HTTP_200_OK)

        return JsonResponse({'message': 'Cập nhật thành công!'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Lỗi, cập nhật không thành công!'}, status=status.HTTP_400_BAD_REQUEST)





class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('User_Name')
            Password = request.POST.get('Password')
            # global user
            user = authenticate(username=username, password=Password)
            if user is not None:
                # Kiểm tra điều kiện hợp lệ ==> Đăng nhập thành công
                login(request, user)
                # return redirect('/location_HTML/')
                user_role = request.user
                finter = Manager_User.objects.all().filter(user=user_role)
                for x in finter:
                    if x.Area == "Giám sát" or x.Area == "Quản trị":
                        return redirect('/location_HTML/')
                    else:
                        return redirect('/info_HTML/')
            else:
                try:
                    # Kiểm tra điều kiện tên người dùng nhập vào có tồn tại hay không
                    User.objects.get(username=username)
                    # Nếu người dùng có tồn tại, nhưng mật khẩu sai ==> Reload lại trang web để người dùng đăng nhập lại
                    messages.error(request, "Sai thông tin đăng nhập!!!!")
                    return redirect('/')
                except User.DoesNotExist:
                    messages.error(request, "Không tồn tại tài khoản này")
                    return redirect('/')

@login_required
def Stats_HTML(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    return render(request, "Stats.html", {'filter':filtered_data})

@login_required
def info_HTML(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    if user.username  == "ThaiMinh":
        nhiet_do_dat, do_am_dat, do_ph, trang_thai_van_khu_vuc_1, trang_thai_van_khu_vuc_2, trang_thai_van_khu_vuc_3, trang_thai_bom, che_do_hoat_dong = get_data(request)
        return render(request, "info.html", {'filter':filtered_data, 'nhiet_do_dat': nhiet_do_dat, 'do_am_dat': do_am_dat, 'do_ph': do_ph, 'trang_thai_van_khu_vuc_1':trang_thai_van_khu_vuc_1, 'trang_thai_van_khu_vuc_2':trang_thai_van_khu_vuc_2, 'trang_thai_van_khu_vuc_3':trang_thai_van_khu_vuc_3, 'trang_thai_bom':trang_thai_bom, 'che_do_hoat_dong':che_do_hoat_dong})
    else:
        return render(request, "info.html", {'filter':filtered_data})

@login_required
def home_HTML(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    if user.username  == "ThaiMinh":
        print('Là Thái Minh')
        if request.method == "POST":
            print("Đã ấn xác nhận")
            kv1_humid = request.POST.get("kv1_humid")
            che_do_tu_dong_gio_bat_dau_tuoi_1 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_1")
            che_do_tu_dong_phut_bat_dau_tuoi_1 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_1")
            che_do_tu_dong_gio_bat_dau_tuoi_2 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_2")
            che_do_tu_dong_phut_bat_dau_tuoi_2 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_2")
            che_do_tu_dong_gio_bat_dau_tuoi_3 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_3")
            che_do_tu_dong_phut_bat_dau_tuoi_3 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_3")
            che_do_tu_dong_gio_bat_dau_tuoi_4 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_4")
            che_do_tu_dong_phut_bat_dau_tuoi_4 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_4")
            che_do_tu_dong_do_am_min_1 = request.POST.get("kv1_range_min_1")
            che_do_tu_dong_do_am_max_1 = request.POST.get("kv1_range_max_1")
            che_do_tu_dong_thoi_gian_tuoi_1 = request.POST.get("kv1_length1")
            che_do_tu_dong_do_am_min_2 = request.POST.get("kv1_range_min_2")
            che_do_tu_dong_do_am_max_2 = request.POST.get("kv1_range_max_2")
            che_do_tu_dong_thoi_gian_tuoi_2 = request.POST.get("kv1_length2")
            che_do_tu_dong_do_am_min_3 = request.POST.get("kv1_range_min_3")
            che_do_tu_dong_do_am_max_3 = request.POST.get("kv1_range_max_3")
            che_do_tu_dong_thoi_gian_tuoi_3 = request.POST.get("kv1_length3")
            che_do_tu_dong_do_am_min_4 = request.POST.get("kv1_range_min_4")
            che_do_tu_dong_do_am_max_4 = request.POST.get("kv1_range_max_4")
            che_do_tu_dong_thoi_gian_tuoi_4 = request.POST.get("kv1_length4")
            url_Update = 'http://mrduck.id.vn/Update_API_ThaiMinh_R_W?change_status=1&che_do_tu_dong_cai_dat_do_am='+kv1_humid+'&che_do_tu_dong_gio_bat_dau_tuoi_1='+che_do_tu_dong_gio_bat_dau_tuoi_1+'&che_do_tu_dong_gio_bat_dau_tuoi_2='+che_do_tu_dong_gio_bat_dau_tuoi_2+'&che_do_tu_dong_gio_bat_dau_tuoi_3='+che_do_tu_dong_gio_bat_dau_tuoi_3+'&che_do_tu_dong_gio_bat_dau_tuoi_4='+che_do_tu_dong_gio_bat_dau_tuoi_4+'&che_do_tu_dong_phut_bat_dau_tuoi_1='+che_do_tu_dong_phut_bat_dau_tuoi_1+'&che_do_tu_dong_phut_bat_dau_tuoi_2='+che_do_tu_dong_phut_bat_dau_tuoi_2+'&che_do_tu_dong_phut_bat_dau_tuoi_3='+che_do_tu_dong_phut_bat_dau_tuoi_3+'&che_do_tu_dong_phut_bat_dau_tuoi_4='+che_do_tu_dong_phut_bat_dau_tuoi_4+'&che_do_tu_dong_do_am_min_1='+che_do_tu_dong_do_am_min_1+'&che_do_tu_dong_do_am_min_2='+che_do_tu_dong_do_am_min_2+'&che_do_tu_dong_do_am_min_3='+che_do_tu_dong_do_am_min_3+'&che_do_tu_dong_do_am_min_4='+che_do_tu_dong_do_am_min_4+'&che_do_tu_dong_do_am_max_1='+che_do_tu_dong_do_am_max_1+'&che_do_tu_dong_do_am_max_2='+che_do_tu_dong_do_am_max_2+'&che_do_tu_dong_do_am_max_3='+che_do_tu_dong_do_am_max_3+'&che_do_tu_dong_do_am_max_4='+che_do_tu_dong_do_am_max_4+'&che_do_tu_dong_thoi_gian_tuoi_1='+che_do_tu_dong_thoi_gian_tuoi_1+'&che_do_tu_dong_thoi_gian_tuoi_2='+che_do_tu_dong_thoi_gian_tuoi_2+'&che_do_tu_dong_thoi_gian_tuoi_3='+che_do_tu_dong_thoi_gian_tuoi_3+'&che_do_tu_dong_thoi_gian_tuoi_4='+che_do_tu_dong_thoi_gian_tuoi_4
            # print(url_Update)
            requests.get(url_Update)

        url_R_W_ThaiMinh = 'http://mrduck.id.vn/Show_API_ThaiMinh_R_W?format=json'
        response_R_W_ThaiMinh = requests.get(url_R_W_ThaiMinh)
        parsed_data_R_W_ThaiMinh = json.loads(response_R_W_ThaiMinh.text)
        # print(parsed_data_R_W_ThaiMinh)
        che_do_tu_dong_gio_bat_dau_tuoi_1 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_gio_bat_dau_tuoi_1']
        che_do_tu_dong_gio_bat_dau_tuoi_2 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_gio_bat_dau_tuoi_2']
        che_do_tu_dong_gio_bat_dau_tuoi_3 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_gio_bat_dau_tuoi_3']
        che_do_tu_dong_gio_bat_dau_tuoi_4 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_gio_bat_dau_tuoi_4']
        che_do_tu_dong_phut_bat_dau_tuoi_1 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_phut_bat_dau_tuoi_1']
        che_do_tu_dong_phut_bat_dau_tuoi_2 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_phut_bat_dau_tuoi_2']
        che_do_tu_dong_phut_bat_dau_tuoi_3 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_phut_bat_dau_tuoi_3']
        che_do_tu_dong_phut_bat_dau_tuoi_4 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_phut_bat_dau_tuoi_4']
        if che_do_tu_dong_gio_bat_dau_tuoi_1 < 10:
            che_do_tu_dong_gio_bat_dau_tuoi_1 = f"0{che_do_tu_dong_gio_bat_dau_tuoi_1}"
        if che_do_tu_dong_gio_bat_dau_tuoi_2 < 10:
            che_do_tu_dong_gio_bat_dau_tuoi_2 = f"0{che_do_tu_dong_gio_bat_dau_tuoi_2}"
        if che_do_tu_dong_gio_bat_dau_tuoi_3 < 10:
            che_do_tu_dong_gio_bat_dau_tuoi_3 = f"0{che_do_tu_dong_gio_bat_dau_tuoi_3}"
        if che_do_tu_dong_gio_bat_dau_tuoi_4 < 10:
            che_do_tu_dong_gio_bat_dau_tuoi_4 = f"0{che_do_tu_dong_gio_bat_dau_tuoi_4}"
        if che_do_tu_dong_phut_bat_dau_tuoi_1 < 10:
            che_do_tu_dong_phut_bat_dau_tuoi_1 = f"0{che_do_tu_dong_phut_bat_dau_tuoi_1}"
        if che_do_tu_dong_phut_bat_dau_tuoi_2 < 10:
            che_do_tu_dong_phut_bat_dau_tuoi_2 = f"0{che_do_tu_dong_phut_bat_dau_tuoi_2}"
        if che_do_tu_dong_phut_bat_dau_tuoi_3 < 10:
            che_do_tu_dong_phut_bat_dau_tuoi_3 = f"0{che_do_tu_dong_phut_bat_dau_tuoi_3}"
        if che_do_tu_dong_phut_bat_dau_tuoi_4 < 10:
            che_do_tu_dong_phut_bat_dau_tuoi_4 = f"0{che_do_tu_dong_phut_bat_dau_tuoi_4}"
        che_do_tu_dong_do_am_min_1 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_do_am_min_1']
        che_do_tu_dong_do_am_min_2 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_do_am_min_2']
        che_do_tu_dong_do_am_min_3 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_do_am_min_3']
        che_do_tu_dong_do_am_min_4 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_do_am_min_4']
        che_do_tu_dong_do_am_max_1 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_do_am_max_1']
        che_do_tu_dong_do_am_max_2 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_do_am_max_2']
        che_do_tu_dong_do_am_max_3 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_do_am_max_3']
        che_do_tu_dong_do_am_max_4 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_do_am_max_4']
        che_do_tu_dong_thoi_gian_tuoi_1 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_thoi_gian_tuoi_1']
        che_do_tu_dong_thoi_gian_tuoi_2 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_thoi_gian_tuoi_2']
        che_do_tu_dong_thoi_gian_tuoi_3 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_thoi_gian_tuoi_3']
        che_do_tu_dong_thoi_gian_tuoi_4 = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_thoi_gian_tuoi_4']
        che_do_tu_dong_cai_dat_do_am = parsed_data_R_W_ThaiMinh[0]['che_do_tu_dong_cai_dat_do_am']
    elif user.username  == "HaoDat":
        print("Là Hảo Đạt")
        if request.method == "POST":
            print("Đã ấn xác nhận")
            kv1_humid = request.POST.get("kv1_humid")
            che_do_tu_dong_gio_bat_dau_tuoi_1 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_1")
            che_do_tu_dong_phut_bat_dau_tuoi_1 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_1")
            che_do_tu_dong_gio_bat_dau_tuoi_2 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_2")
            che_do_tu_dong_phut_bat_dau_tuoi_2 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_2")
            che_do_tu_dong_gio_bat_dau_tuoi_3 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_3")
            che_do_tu_dong_phut_bat_dau_tuoi_3 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_3")
            che_do_tu_dong_gio_bat_dau_tuoi_4 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_4")
            che_do_tu_dong_phut_bat_dau_tuoi_4 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_4")
            che_do_tu_dong_do_am_min_1 = request.POST.get("kv1_range_min_1")
            che_do_tu_dong_do_am_max_1 = request.POST.get("kv1_range_max_1")
            che_do_tu_dong_thoi_gian_tuoi_1 = request.POST.get("kv1_length1")
            che_do_tu_dong_do_am_min_2 = request.POST.get("kv1_range_min_2")
            che_do_tu_dong_do_am_max_2 = request.POST.get("kv1_range_max_2")
            che_do_tu_dong_thoi_gian_tuoi_2 = request.POST.get("kv1_length2")
            che_do_tu_dong_do_am_min_3 = request.POST.get("kv1_range_min_3")
            che_do_tu_dong_do_am_max_3 = request.POST.get("kv1_range_max_3")
            che_do_tu_dong_thoi_gian_tuoi_3 = request.POST.get("kv1_length3")
            che_do_tu_dong_do_am_min_4 = request.POST.get("kv1_range_min_4")
            che_do_tu_dong_do_am_max_4 = request.POST.get("kv1_range_max_4")
            che_do_tu_dong_thoi_gian_tuoi_4 = request.POST.get("kv1_length4")
            url_Update = 'http://mrduck.id.vn/Update_API_HaoDat_R_W?change_status=1&che_do_tu_dong_cai_dat_do_am='+kv1_humid+'&che_do_tu_dong_gio_bat_dau_tuoi_1='+che_do_tu_dong_gio_bat_dau_tuoi_1+'&che_do_tu_dong_gio_bat_dau_tuoi_2='+che_do_tu_dong_gio_bat_dau_tuoi_2+'&che_do_tu_dong_gio_bat_dau_tuoi_3='+che_do_tu_dong_gio_bat_dau_tuoi_3+'&che_do_tu_dong_gio_bat_dau_tuoi_4='+che_do_tu_dong_gio_bat_dau_tuoi_4+'&che_do_tu_dong_phut_bat_dau_tuoi_1='+che_do_tu_dong_phut_bat_dau_tuoi_1+'&che_do_tu_dong_phut_bat_dau_tuoi_2='+che_do_tu_dong_phut_bat_dau_tuoi_2+'&che_do_tu_dong_phut_bat_dau_tuoi_3='+che_do_tu_dong_phut_bat_dau_tuoi_3+'&che_do_tu_dong_phut_bat_dau_tuoi_4='+che_do_tu_dong_phut_bat_dau_tuoi_4+'&che_do_tu_dong_do_am_min_1='+che_do_tu_dong_do_am_min_1+'&che_do_tu_dong_do_am_min_2='+che_do_tu_dong_do_am_min_2+'&che_do_tu_dong_do_am_min_3='+che_do_tu_dong_do_am_min_3+'&che_do_tu_dong_do_am_min_4='+che_do_tu_dong_do_am_min_4+'&che_do_tu_dong_do_am_max_1='+che_do_tu_dong_do_am_max_1+'&che_do_tu_dong_do_am_max_2='+che_do_tu_dong_do_am_max_2+'&che_do_tu_dong_do_am_max_3='+che_do_tu_dong_do_am_max_3+'&che_do_tu_dong_do_am_max_4='+che_do_tu_dong_do_am_max_4+'&che_do_tu_dong_thoi_gian_tuoi_1='+che_do_tu_dong_thoi_gian_tuoi_1+'&che_do_tu_dong_thoi_gian_tuoi_2='+che_do_tu_dong_thoi_gian_tuoi_2+'&che_do_tu_dong_thoi_gian_tuoi_3='+che_do_tu_dong_thoi_gian_tuoi_3+'&che_do_tu_dong_thoi_gian_tuoi_4='+che_do_tu_dong_thoi_gian_tuoi_4
            # print(url_Update)
            requests.get(url_Update)

        url_R_W_HaoDat = 'http://mrduck.id.vn/Show_API_HaoDat_R_W?format=json'
        response_R_W_HaoDat = requests.get(url_R_W_HaoDat)
        parsed_data_R_W_HaoDat = json.loads(response_R_W_HaoDat.text)
        che_do_tu_dong_gio_bat_dau_tuoi_1 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_gio_bat_dau_tuoi_1']
        che_do_tu_dong_gio_bat_dau_tuoi_2 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_gio_bat_dau_tuoi_2']
        che_do_tu_dong_gio_bat_dau_tuoi_3 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_gio_bat_dau_tuoi_3']
        che_do_tu_dong_gio_bat_dau_tuoi_4 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_gio_bat_dau_tuoi_4']
        che_do_tu_dong_phut_bat_dau_tuoi_1 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_phut_bat_dau_tuoi_1']
        che_do_tu_dong_phut_bat_dau_tuoi_2 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_phut_bat_dau_tuoi_2']
        che_do_tu_dong_phut_bat_dau_tuoi_3 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_phut_bat_dau_tuoi_3']
        che_do_tu_dong_phut_bat_dau_tuoi_4 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_phut_bat_dau_tuoi_4']
        che_do_tu_dong_do_am_min_1 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_do_am_min_1']
        che_do_tu_dong_do_am_min_2 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_do_am_min_2']
        che_do_tu_dong_do_am_min_3 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_do_am_min_3']
        che_do_tu_dong_do_am_min_4 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_do_am_min_4']
        che_do_tu_dong_do_am_max_1 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_do_am_max_1']
        che_do_tu_dong_do_am_max_2 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_do_am_max_2']
        che_do_tu_dong_do_am_max_3 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_do_am_max_3']
        che_do_tu_dong_do_am_max_4 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_do_am_max_4']
        che_do_tu_dong_thoi_gian_tuoi_1 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_thoi_gian_tuoi_1']
        che_do_tu_dong_thoi_gian_tuoi_2 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_thoi_gian_tuoi_2']
        che_do_tu_dong_thoi_gian_tuoi_3 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_thoi_gian_tuoi_3']
        che_do_tu_dong_thoi_gian_tuoi_4 = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_thoi_gian_tuoi_4']
        che_do_tu_dong_cai_dat_do_am = parsed_data_R_W_HaoDat[0]['che_do_tu_dong_cai_dat_do_am']
    elif user.username  == "KheCoc":
        print("Là Khe Cốc")
        if request.method == "POST":
            print("Đã ấn xác nhận")
            kv1_humid = request.POST.get("kv1_humid")
            che_do_tu_dong_gio_bat_dau_tuoi_1 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_1")
            che_do_tu_dong_phut_bat_dau_tuoi_1 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_1")
            che_do_tu_dong_gio_bat_dau_tuoi_2 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_2")
            che_do_tu_dong_phut_bat_dau_tuoi_2 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_2")
            che_do_tu_dong_gio_bat_dau_tuoi_3 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_3")
            che_do_tu_dong_phut_bat_dau_tuoi_3 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_3")
            che_do_tu_dong_gio_bat_dau_tuoi_4 = request.POST.get("che_do_tu_dong_gio_bat_dau_tuoi_4")
            che_do_tu_dong_phut_bat_dau_tuoi_4 = request.POST.get("che_do_tu_dong_phut_bat_dau_tuoi_4")
            che_do_tu_dong_do_am_min_1 = request.POST.get("kv1_range_min_1")
            che_do_tu_dong_do_am_max_1 = request.POST.get("kv1_range_max_1")
            che_do_tu_dong_thoi_gian_tuoi_1 = request.POST.get("kv1_length1")
            che_do_tu_dong_do_am_min_2 = request.POST.get("kv1_range_min_2")
            che_do_tu_dong_do_am_max_2 = request.POST.get("kv1_range_max_2")
            che_do_tu_dong_thoi_gian_tuoi_2 = request.POST.get("kv1_length2")
            che_do_tu_dong_do_am_min_3 = request.POST.get("kv1_range_min_3")
            che_do_tu_dong_do_am_max_3 = request.POST.get("kv1_range_max_3")
            che_do_tu_dong_thoi_gian_tuoi_3 = request.POST.get("kv1_length3")
            che_do_tu_dong_do_am_min_4 = request.POST.get("kv1_range_min_4")
            che_do_tu_dong_do_am_max_4 = request.POST.get("kv1_range_max_4")
            che_do_tu_dong_thoi_gian_tuoi_4 = request.POST.get("kv1_length4")
            url_Update = 'http://mrduck.id.vn/Update_API_KheCoc_R_W?change_status=1&che_do_tu_dong_cai_dat_do_am='+kv1_humid+'&che_do_tu_dong_gio_bat_dau_tuoi_1='+che_do_tu_dong_gio_bat_dau_tuoi_1+'&che_do_tu_dong_gio_bat_dau_tuoi_2='+che_do_tu_dong_gio_bat_dau_tuoi_2+'&che_do_tu_dong_gio_bat_dau_tuoi_3='+che_do_tu_dong_gio_bat_dau_tuoi_3+'&che_do_tu_dong_gio_bat_dau_tuoi_4='+che_do_tu_dong_gio_bat_dau_tuoi_4+'&che_do_tu_dong_phut_bat_dau_tuoi_1='+che_do_tu_dong_phut_bat_dau_tuoi_1+'&che_do_tu_dong_phut_bat_dau_tuoi_2='+che_do_tu_dong_phut_bat_dau_tuoi_2+'&che_do_tu_dong_phut_bat_dau_tuoi_3='+che_do_tu_dong_phut_bat_dau_tuoi_3+'&che_do_tu_dong_phut_bat_dau_tuoi_4='+che_do_tu_dong_phut_bat_dau_tuoi_4+'&che_do_tu_dong_do_am_min_1='+che_do_tu_dong_do_am_min_1+'&che_do_tu_dong_do_am_min_2='+che_do_tu_dong_do_am_min_2+'&che_do_tu_dong_do_am_min_3='+che_do_tu_dong_do_am_min_3+'&che_do_tu_dong_do_am_min_4='+che_do_tu_dong_do_am_min_4+'&che_do_tu_dong_do_am_max_1='+che_do_tu_dong_do_am_max_1+'&che_do_tu_dong_do_am_max_2='+che_do_tu_dong_do_am_max_2+'&che_do_tu_dong_do_am_max_3='+che_do_tu_dong_do_am_max_3+'&che_do_tu_dong_do_am_max_4='+che_do_tu_dong_do_am_max_4+'&che_do_tu_dong_thoi_gian_tuoi_1='+che_do_tu_dong_thoi_gian_tuoi_1+'&che_do_tu_dong_thoi_gian_tuoi_2='+che_do_tu_dong_thoi_gian_tuoi_2+'&che_do_tu_dong_thoi_gian_tuoi_3='+che_do_tu_dong_thoi_gian_tuoi_3+'&che_do_tu_dong_thoi_gian_tuoi_4='+che_do_tu_dong_thoi_gian_tuoi_4
            # print(url_Update)
            # requests.get(url_Update)
        url_R_W_KheCoc = 'http://mrduck.id.vn/Show_API_KheCoc_R_W?format=json'
        response_R_W_KheCoc = requests.get(url_R_W_KheCoc)
        response_R_W_KheCoc = json.loads(response_R_W_KheCoc.text)
        che_do_tu_dong_gio_bat_dau_tuoi_1 = response_R_W_KheCoc[0]['che_do_tu_dong_gio_bat_dau_tuoi_1']
        che_do_tu_dong_gio_bat_dau_tuoi_2 = response_R_W_KheCoc[0]['che_do_tu_dong_gio_bat_dau_tuoi_2']
        che_do_tu_dong_gio_bat_dau_tuoi_3 = response_R_W_KheCoc[0]['che_do_tu_dong_gio_bat_dau_tuoi_3']
        che_do_tu_dong_gio_bat_dau_tuoi_4 = response_R_W_KheCoc[0]['che_do_tu_dong_gio_bat_dau_tuoi_4']
        che_do_tu_dong_phut_bat_dau_tuoi_1 = response_R_W_KheCoc[0]['che_do_tu_dong_phut_bat_dau_tuoi_1']
        che_do_tu_dong_phut_bat_dau_tuoi_2 = response_R_W_KheCoc[0]['che_do_tu_dong_phut_bat_dau_tuoi_2']
        che_do_tu_dong_phut_bat_dau_tuoi_3 = response_R_W_KheCoc[0]['che_do_tu_dong_phut_bat_dau_tuoi_3']
        che_do_tu_dong_phut_bat_dau_tuoi_4 = response_R_W_KheCoc[0]['che_do_tu_dong_phut_bat_dau_tuoi_4']
        che_do_tu_dong_do_am_min_1 = response_R_W_KheCoc[0]['che_do_tu_dong_do_am_min_1']
        che_do_tu_dong_do_am_min_2 = response_R_W_KheCoc[0]['che_do_tu_dong_do_am_min_2']
        che_do_tu_dong_do_am_min_3 = response_R_W_KheCoc[0]['che_do_tu_dong_do_am_min_3']
        che_do_tu_dong_do_am_min_4 = response_R_W_KheCoc[0]['che_do_tu_dong_do_am_min_4']
        che_do_tu_dong_do_am_max_1 = response_R_W_KheCoc[0]['che_do_tu_dong_do_am_max_1']
        che_do_tu_dong_do_am_max_2 = response_R_W_KheCoc[0]['che_do_tu_dong_do_am_max_2']
        che_do_tu_dong_do_am_max_3 = response_R_W_KheCoc[0]['che_do_tu_dong_do_am_max_3']
        che_do_tu_dong_do_am_max_4 = response_R_W_KheCoc[0]['che_do_tu_dong_do_am_max_4']
        che_do_tu_dong_thoi_gian_tuoi_1 = response_R_W_KheCoc[0]['che_do_tu_dong_thoi_gian_tuoi_1']
        che_do_tu_dong_thoi_gian_tuoi_2 = response_R_W_KheCoc[0]['che_do_tu_dong_thoi_gian_tuoi_2']
        che_do_tu_dong_thoi_gian_tuoi_3 = response_R_W_KheCoc[0]['che_do_tu_dong_thoi_gian_tuoi_3']
        che_do_tu_dong_thoi_gian_tuoi_4 = response_R_W_KheCoc[0]['che_do_tu_dong_thoi_gian_tuoi_4']
        che_do_tu_dong_cai_dat_do_am = response_R_W_KheCoc[0]['che_do_tu_dong_cai_dat_do_am']
    return render(request, "home.html", {'filter':filtered_data, 'che_do_tu_dong_gio_bat_dau_tuoi_1':che_do_tu_dong_gio_bat_dau_tuoi_1, 'che_do_tu_dong_gio_bat_dau_tuoi_2':che_do_tu_dong_gio_bat_dau_tuoi_2, 'che_do_tu_dong_gio_bat_dau_tuoi_3':che_do_tu_dong_gio_bat_dau_tuoi_3, 'che_do_tu_dong_gio_bat_dau_tuoi_4':che_do_tu_dong_gio_bat_dau_tuoi_4, 'che_do_tu_dong_phut_bat_dau_tuoi_1':che_do_tu_dong_phut_bat_dau_tuoi_1, 'che_do_tu_dong_phut_bat_dau_tuoi_2':che_do_tu_dong_phut_bat_dau_tuoi_2, 'che_do_tu_dong_phut_bat_dau_tuoi_3':che_do_tu_dong_phut_bat_dau_tuoi_3, 'che_do_tu_dong_phut_bat_dau_tuoi_4':che_do_tu_dong_phut_bat_dau_tuoi_4, 'che_do_tu_dong_do_am_min_1':che_do_tu_dong_do_am_min_1, 'che_do_tu_dong_do_am_min_2':che_do_tu_dong_do_am_min_2, 'che_do_tu_dong_do_am_min_3':che_do_tu_dong_do_am_min_3, 'che_do_tu_dong_do_am_min_4':che_do_tu_dong_do_am_min_4, 'che_do_tu_dong_do_am_max_1':che_do_tu_dong_do_am_max_1, 'che_do_tu_dong_do_am_max_2':che_do_tu_dong_do_am_max_2, 'che_do_tu_dong_do_am_max_3':che_do_tu_dong_do_am_max_3, 'che_do_tu_dong_do_am_max_4':che_do_tu_dong_do_am_max_4, 'che_do_tu_dong_thoi_gian_tuoi_1':che_do_tu_dong_thoi_gian_tuoi_1, 'che_do_tu_dong_thoi_gian_tuoi_2':che_do_tu_dong_thoi_gian_tuoi_2, 'che_do_tu_dong_thoi_gian_tuoi_3':che_do_tu_dong_thoi_gian_tuoi_3, 'che_do_tu_dong_thoi_gian_tuoi_4':che_do_tu_dong_thoi_gian_tuoi_4, 'che_do_tu_dong_cai_dat_do_am':che_do_tu_dong_cai_dat_do_am})

@login_required
def daily_HTML(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    if user.username  == "ThaiMinh":
        print('Là Thái Minh')
        if request.method == "POST":
            che_do_hang_ngay_xac_nhan_lan_1 = request.POST.get('day_1')
            if che_do_hang_ngay_xac_nhan_lan_1 == '1':
                che_do_hang_ngay_xac_nhan_lan_1 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_1 != '1':
                che_do_hang_ngay_xac_nhan_lan_1 = '0'
            che_do_hang_ngay_xac_nhan_lan_2 = request.POST.get('day_2')
            if che_do_hang_ngay_xac_nhan_lan_2 == '1':
                che_do_hang_ngay_xac_nhan_lan_2 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_2 != '1':
                che_do_hang_ngay_xac_nhan_lan_2 = '0'
            che_do_hang_ngay_xac_nhan_lan_3 = request.POST.get('day_3')
            if che_do_hang_ngay_xac_nhan_lan_3 == '1':
                che_do_hang_ngay_xac_nhan_lan_3 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_3 != '1':
                che_do_hang_ngay_xac_nhan_lan_3 = '0'
            che_do_hang_ngay_xac_nhan_lan_4 = request.POST.get('day_4')
            if che_do_hang_ngay_xac_nhan_lan_4 == '1':
                che_do_hang_ngay_xac_nhan_lan_4 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_4 != '1':
                che_do_hang_ngay_xac_nhan_lan_4 = '0'
            area_1_1 = request.POST.get('area_1_1')
            print(area_1_1)
            if area_1_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_1_1 = '1'
            elif area_1_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_1_1 = '0'
            area_1_2 = request.POST.get('area_1_2')
            if area_1_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_1_2 = '1'
            elif area_1_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_1_2 = '0'
            area_1_3 = request.POST.get('area_1_3')
            if area_1_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_1_3 = '1'
            elif area_1_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_1_3 = '0'
            area_2_1 = request.POST.get('area_2_1')
            if area_2_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_2_1 = '1'
            elif area_2_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_2_1 = '0'
            area_2_2 = request.POST.get('area_2_2')
            if area_2_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_2_2 = '1'
            elif area_2_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_2_2 = '0'
            area_2_3 = request.POST.get('area_2_3')
            if area_2_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_2_3 = '1'
            elif area_2_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_2_3 = '0'
            area_3_1 = request.POST.get('area_3_1')
            if area_3_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_3_1 = '1'
            elif area_3_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_3_1 = '0'
            area_3_2 = request.POST.get('area_3_2')
            if area_3_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_3_2 = '1'
            elif area_3_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_3_2 = '0'
            area_3_3 = request.POST.get('area_3_3')
            if area_3_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_3_3 = '1'
            elif area_3_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_3_3 = '0'
            area_4_1 = request.POST.get('area_4_1')
            if area_4_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_4_1 = '1'
            elif area_4_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_4_1 = '0'
            area_4_2 = request.POST.get('area_4_2')
            if area_4_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_4_2 = '1'
            elif area_4_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_4_2 = '0'
            area_4_3 = request.POST.get('area_4_3')
            if area_4_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_4_3 = '1'
            elif area_4_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_4_3 = '0'
            
            che_do_hang_ngay_gio_bat_dau_tuoi_1 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_1')
            che_do_hang_ngay_gio_bat_dau_tuoi_2 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_2')
            che_do_hang_ngay_gio_bat_dau_tuoi_3 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_3')
            che_do_hang_ngay_gio_bat_dau_tuoi_4 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_4')
            che_do_hang_ngay_phut_bat_dau_tuoi_1 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_1')
            che_do_hang_ngay_phut_bat_dau_tuoi_2 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_2')
            che_do_hang_ngay_phut_bat_dau_tuoi_3 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_3')
            che_do_hang_ngay_phut_bat_dau_tuoi_4 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_4')
            che_do_hang_ngay_thoi_gian_tuoi_1 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_1')
            che_do_hang_ngay_thoi_gian_tuoi_2 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_2')
            che_do_hang_ngay_thoi_gian_tuoi_3 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_3')
            che_do_hang_ngay_thoi_gian_tuoi_4 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_4')
            # print('che_do_hang_ngay_xac_nhan_lan_1='+che_do_hang_ngay_xac_nhan_lan_1+'&che_do_hang_ngay_xac_nhan_lan_2='+che_do_hang_ngay_xac_nhan_lan_2+'&che_do_hang_ngay_xac_nhan_lan_3='+che_do_hang_ngay_xac_nhan_lan_3+'&che_do_hang_ngay_xac_nhan_lan_4='+che_do_hang_ngay_xac_nhan_lan_4+'&che_do_hang_ngay_dieu_khien_KV_1_1='+che_do_hang_ngay_dieu_khien_KV_1_1+'&che_do_hang_ngay_dieu_khien_KV_1_2='+che_do_hang_ngay_dieu_khien_KV_1_2+'&che_do_hang_ngay_dieu_khien_KV_1_3='+che_do_hang_ngay_dieu_khien_KV_1_3+'&che_do_hang_ngay_dieu_khien_KV_2_1='+che_do_hang_ngay_dieu_khien_KV_2_1+'&che_do_hang_ngay_dieu_khien_KV_2_2='+che_do_hang_ngay_dieu_khien_KV_2_2+'&che_do_hang_ngay_dieu_khien_KV_2_3='+che_do_hang_ngay_dieu_khien_KV_2_3+'&che_do_hang_ngay_dieu_khien_KV_3_1='+che_do_hang_ngay_dieu_khien_KV_3_1+'&che_do_hang_ngay_dieu_khien_KV_3_2='+che_do_hang_ngay_dieu_khien_KV_3_2+'&che_do_hang_ngay_dieu_khien_KV_3_3='+che_do_hang_ngay_dieu_khien_KV_3_3+'&che_do_hang_ngay_dieu_khien_KV_4_1='+che_do_hang_ngay_dieu_khien_KV_4_1+'&che_do_hang_ngay_dieu_khien_KV_4_2='+che_do_hang_ngay_dieu_khien_KV_4_2+'&che_do_hang_ngay_dieu_khien_KV_4_3='+che_do_hang_ngay_dieu_khien_KV_4_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_1='+che_do_hang_ngay_gio_bat_dau_tuoi_1+'&che_do_hang_ngay_gio_bat_dau_tuoi_2='+che_do_hang_ngay_gio_bat_dau_tuoi_2+'&che_do_hang_ngay_gio_bat_dau_tuoi_3='+che_do_hang_ngay_gio_bat_dau_tuoi_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_4='+che_do_hang_ngay_gio_bat_dau_tuoi_4+'&che_do_hang_ngay_phut_bat_dau_tuoi_1='+che_do_hang_ngay_phut_bat_dau_tuoi_1+'&che_do_hang_ngay_phut_bat_dau_tuoi_2='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_3='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_4='+che_do_hang_ngay_phut_bat_dau_tuoi_4+'&che_do_hang_ngay_thoi_gian_tuoi_1='+che_do_hang_ngay_thoi_gian_tuoi_1+'&che_do_hang_ngay_thoi_gian_tuoi_2='+che_do_hang_ngay_thoi_gian_tuoi_2+'&che_do_hang_ngay_thoi_gian_tuoi_3='+che_do_hang_ngay_thoi_gian_tuoi_3+'&che_do_hang_ngay_thoi_gian_tuoi_4='+che_do_hang_ngay_thoi_gian_tuoi_4)
            url_Update = 'http://mrduck.id.vn/Update_API_ThaiMinh_R_W?change_status=99&che_do_hang_ngay_xac_nhan_lan_1='+che_do_hang_ngay_xac_nhan_lan_1+'&che_do_hang_ngay_xac_nhan_lan_2='+che_do_hang_ngay_xac_nhan_lan_2+'&che_do_hang_ngay_xac_nhan_lan_3='+che_do_hang_ngay_xac_nhan_lan_3+'&che_do_hang_ngay_xac_nhan_lan_4='+che_do_hang_ngay_xac_nhan_lan_4+'&che_do_hang_ngay_dieu_khien_KV_1_1='+che_do_hang_ngay_dieu_khien_KV_1_1+'&che_do_hang_ngay_dieu_khien_KV_1_2='+che_do_hang_ngay_dieu_khien_KV_1_2+'&che_do_hang_ngay_dieu_khien_KV_1_3='+che_do_hang_ngay_dieu_khien_KV_1_3+'&che_do_hang_ngay_dieu_khien_KV_2_1='+che_do_hang_ngay_dieu_khien_KV_2_1+'&che_do_hang_ngay_dieu_khien_KV_2_2='+che_do_hang_ngay_dieu_khien_KV_2_2+'&che_do_hang_ngay_dieu_khien_KV_2_3='+che_do_hang_ngay_dieu_khien_KV_2_3+'&che_do_hang_ngay_dieu_khien_KV_3_1='+che_do_hang_ngay_dieu_khien_KV_3_1+'&che_do_hang_ngay_dieu_khien_KV_3_2='+che_do_hang_ngay_dieu_khien_KV_3_2+'&che_do_hang_ngay_dieu_khien_KV_3_3='+che_do_hang_ngay_dieu_khien_KV_3_3+'&che_do_hang_ngay_dieu_khien_KV_4_1='+che_do_hang_ngay_dieu_khien_KV_4_1+'&che_do_hang_ngay_dieu_khien_KV_4_2='+che_do_hang_ngay_dieu_khien_KV_4_2+'&che_do_hang_ngay_dieu_khien_KV_4_3='+che_do_hang_ngay_dieu_khien_KV_4_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_1='+che_do_hang_ngay_gio_bat_dau_tuoi_1+'&che_do_hang_ngay_gio_bat_dau_tuoi_2='+che_do_hang_ngay_gio_bat_dau_tuoi_2+'&che_do_hang_ngay_gio_bat_dau_tuoi_3='+che_do_hang_ngay_gio_bat_dau_tuoi_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_4='+che_do_hang_ngay_gio_bat_dau_tuoi_4+'&che_do_hang_ngay_phut_bat_dau_tuoi_1='+che_do_hang_ngay_phut_bat_dau_tuoi_1+'&che_do_hang_ngay_phut_bat_dau_tuoi_2='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_3='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_4='+che_do_hang_ngay_phut_bat_dau_tuoi_4+'&che_do_hang_ngay_thoi_gian_tuoi_1='+che_do_hang_ngay_thoi_gian_tuoi_1+'&che_do_hang_ngay_thoi_gian_tuoi_2='+che_do_hang_ngay_thoi_gian_tuoi_2+'&che_do_hang_ngay_thoi_gian_tuoi_3='+che_do_hang_ngay_thoi_gian_tuoi_3+'&che_do_hang_ngay_thoi_gian_tuoi_4='+che_do_hang_ngay_thoi_gian_tuoi_4
            # print(url_Update)
            requests.get(url_Update)

        url_R_W_ThaiMinh = 'http://mrduck.id.vn/Show_API_ThaiMinh_R_W?format=json'
        response_R_W_ThaiMinh = requests.get(url_R_W_ThaiMinh)
        parsed_data_R_W_ThaiMinh = json.loads(response_R_W_ThaiMinh.text)
        # print(parsed_data_R_W_ThaiMinh)
        che_do_hang_ngay_xac_nhan_lan_1 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_xac_nhan_lan_1']
        che_do_hang_ngay_xac_nhan_lan_2 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_xac_nhan_lan_2']
        che_do_hang_ngay_xac_nhan_lan_3 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_xac_nhan_lan_3']
        che_do_hang_ngay_xac_nhan_lan_4 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_xac_nhan_lan_4']
        che_do_hang_ngay_dieu_khien_KV_1_1 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_1_1']
        che_do_hang_ngay_dieu_khien_KV_1_2 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_1_2']
        che_do_hang_ngay_dieu_khien_KV_1_3 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_1_3']
        che_do_hang_ngay_dieu_khien_KV_2_1 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_2_1']
        che_do_hang_ngay_dieu_khien_KV_2_2 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_2_2']
        che_do_hang_ngay_dieu_khien_KV_2_3 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_2_3']
        che_do_hang_ngay_dieu_khien_KV_3_1 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_3_1']
        che_do_hang_ngay_dieu_khien_KV_3_2 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_3_2']
        che_do_hang_ngay_dieu_khien_KV_3_3 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_3_3']
        che_do_hang_ngay_dieu_khien_KV_4_1 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_4_1']
        che_do_hang_ngay_dieu_khien_KV_4_2 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_4_2']
        che_do_hang_ngay_dieu_khien_KV_4_3 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_dieu_khien_KV_4_3']

        che_do_hang_ngay_thoi_gian_tuoi_1 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_thoi_gian_tuoi_1']
        che_do_hang_ngay_thoi_gian_tuoi_2 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_thoi_gian_tuoi_2']
        che_do_hang_ngay_thoi_gian_tuoi_3 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_thoi_gian_tuoi_3']
        che_do_hang_ngay_thoi_gian_tuoi_4 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_thoi_gian_tuoi_4']
        che_do_hang_ngay_gio_bat_dau_tuoi_1 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_gio_bat_dau_tuoi_1']
        che_do_hang_ngay_gio_bat_dau_tuoi_2 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_gio_bat_dau_tuoi_2']
        che_do_hang_ngay_gio_bat_dau_tuoi_3 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_gio_bat_dau_tuoi_3']
        che_do_hang_ngay_gio_bat_dau_tuoi_4 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_gio_bat_dau_tuoi_4']
        che_do_hang_ngay_phut_bat_dau_tuoi_1 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_phut_bat_dau_tuoi_1']
        che_do_hang_ngay_phut_bat_dau_tuoi_2 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_phut_bat_dau_tuoi_2']
        che_do_hang_ngay_phut_bat_dau_tuoi_3 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_phut_bat_dau_tuoi_3']
        che_do_hang_ngay_phut_bat_dau_tuoi_4 = parsed_data_R_W_ThaiMinh[0]['che_do_hang_ngay_phut_bat_dau_tuoi_4']
    elif user.username  == "HaoDat":
        print('Là Hảo Đạt')
        if request.method == "POST":
            che_do_hang_ngay_xac_nhan_lan_1 = request.POST.get('day_1')
            if che_do_hang_ngay_xac_nhan_lan_1 == '1':
                che_do_hang_ngay_xac_nhan_lan_1 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_1 != '1':
                che_do_hang_ngay_xac_nhan_lan_1 = '0'
            che_do_hang_ngay_xac_nhan_lan_2 = request.POST.get('day_2')
            if che_do_hang_ngay_xac_nhan_lan_2 == '1':
                che_do_hang_ngay_xac_nhan_lan_2 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_2 != '1':
                che_do_hang_ngay_xac_nhan_lan_2 = '0'
            che_do_hang_ngay_xac_nhan_lan_3 = request.POST.get('day_3')
            if che_do_hang_ngay_xac_nhan_lan_3 == '1':
                che_do_hang_ngay_xac_nhan_lan_3 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_3 != '1':
                che_do_hang_ngay_xac_nhan_lan_3 = '0'
            che_do_hang_ngay_xac_nhan_lan_4 = request.POST.get('day_4')
            if che_do_hang_ngay_xac_nhan_lan_4 == '1':
                che_do_hang_ngay_xac_nhan_lan_4 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_4 != '1':
                che_do_hang_ngay_xac_nhan_lan_4 = '0'
            area_1_1 = request.POST.get('area_1_1')
            print(area_1_1)
            if area_1_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_1_1 = '1'
            elif area_1_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_1_1 = '0'
            area_1_2 = request.POST.get('area_1_2')
            if area_1_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_1_2 = '1'
            elif area_1_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_1_2 = '0'
            area_1_3 = request.POST.get('area_1_3')
            if area_1_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_1_3 = '1'
            elif area_1_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_1_3 = '0'
            area_2_1 = request.POST.get('area_2_1')
            if area_2_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_2_1 = '1'
            elif area_2_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_2_1 = '0'
            area_2_2 = request.POST.get('area_2_2')
            if area_2_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_2_2 = '1'
            elif area_2_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_2_2 = '0'
            area_2_3 = request.POST.get('area_2_3')
            if area_2_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_2_3 = '1'
            elif area_2_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_2_3 = '0'
            area_3_1 = request.POST.get('area_3_1')
            if area_3_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_3_1 = '1'
            elif area_3_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_3_1 = '0'
            area_3_2 = request.POST.get('area_3_2')
            if area_3_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_3_2 = '1'
            elif area_3_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_3_2 = '0'
            area_3_3 = request.POST.get('area_3_3')
            if area_3_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_3_3 = '1'
            elif area_3_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_3_3 = '0'
            area_4_1 = request.POST.get('area_4_1')
            if area_4_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_4_1 = '1'
            elif area_4_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_4_1 = '0'
            area_4_2 = request.POST.get('area_4_2')
            if area_4_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_4_2 = '1'
            elif area_4_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_4_2 = '0'
            area_4_3 = request.POST.get('area_4_3')
            if area_4_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_4_3 = '1'
            elif area_4_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_4_3 = '0'
            
            che_do_hang_ngay_gio_bat_dau_tuoi_1 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_1')
            che_do_hang_ngay_gio_bat_dau_tuoi_2 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_2')
            che_do_hang_ngay_gio_bat_dau_tuoi_3 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_3')
            che_do_hang_ngay_gio_bat_dau_tuoi_4 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_4')
            che_do_hang_ngay_phut_bat_dau_tuoi_1 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_1')
            che_do_hang_ngay_phut_bat_dau_tuoi_2 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_2')
            che_do_hang_ngay_phut_bat_dau_tuoi_3 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_3')
            che_do_hang_ngay_phut_bat_dau_tuoi_4 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_4')
            che_do_hang_ngay_thoi_gian_tuoi_1 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_1')
            che_do_hang_ngay_thoi_gian_tuoi_2 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_2')
            che_do_hang_ngay_thoi_gian_tuoi_3 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_3')
            che_do_hang_ngay_thoi_gian_tuoi_4 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_4')
            # print('che_do_hang_ngay_xac_nhan_lan_1='+che_do_hang_ngay_xac_nhan_lan_1+'&che_do_hang_ngay_xac_nhan_lan_2='+che_do_hang_ngay_xac_nhan_lan_2+'&che_do_hang_ngay_xac_nhan_lan_3='+che_do_hang_ngay_xac_nhan_lan_3+'&che_do_hang_ngay_xac_nhan_lan_4='+che_do_hang_ngay_xac_nhan_lan_4+'&che_do_hang_ngay_dieu_khien_KV_1_1='+che_do_hang_ngay_dieu_khien_KV_1_1+'&che_do_hang_ngay_dieu_khien_KV_1_2='+che_do_hang_ngay_dieu_khien_KV_1_2+'&che_do_hang_ngay_dieu_khien_KV_1_3='+che_do_hang_ngay_dieu_khien_KV_1_3+'&che_do_hang_ngay_dieu_khien_KV_2_1='+che_do_hang_ngay_dieu_khien_KV_2_1+'&che_do_hang_ngay_dieu_khien_KV_2_2='+che_do_hang_ngay_dieu_khien_KV_2_2+'&che_do_hang_ngay_dieu_khien_KV_2_3='+che_do_hang_ngay_dieu_khien_KV_2_3+'&che_do_hang_ngay_dieu_khien_KV_3_1='+che_do_hang_ngay_dieu_khien_KV_3_1+'&che_do_hang_ngay_dieu_khien_KV_3_2='+che_do_hang_ngay_dieu_khien_KV_3_2+'&che_do_hang_ngay_dieu_khien_KV_3_3='+che_do_hang_ngay_dieu_khien_KV_3_3+'&che_do_hang_ngay_dieu_khien_KV_4_1='+che_do_hang_ngay_dieu_khien_KV_4_1+'&che_do_hang_ngay_dieu_khien_KV_4_2='+che_do_hang_ngay_dieu_khien_KV_4_2+'&che_do_hang_ngay_dieu_khien_KV_4_3='+che_do_hang_ngay_dieu_khien_KV_4_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_1='+che_do_hang_ngay_gio_bat_dau_tuoi_1+'&che_do_hang_ngay_gio_bat_dau_tuoi_2='+che_do_hang_ngay_gio_bat_dau_tuoi_2+'&che_do_hang_ngay_gio_bat_dau_tuoi_3='+che_do_hang_ngay_gio_bat_dau_tuoi_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_4='+che_do_hang_ngay_gio_bat_dau_tuoi_4+'&che_do_hang_ngay_phut_bat_dau_tuoi_1='+che_do_hang_ngay_phut_bat_dau_tuoi_1+'&che_do_hang_ngay_phut_bat_dau_tuoi_2='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_3='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_4='+che_do_hang_ngay_phut_bat_dau_tuoi_4+'&che_do_hang_ngay_thoi_gian_tuoi_1='+che_do_hang_ngay_thoi_gian_tuoi_1+'&che_do_hang_ngay_thoi_gian_tuoi_2='+che_do_hang_ngay_thoi_gian_tuoi_2+'&che_do_hang_ngay_thoi_gian_tuoi_3='+che_do_hang_ngay_thoi_gian_tuoi_3+'&che_do_hang_ngay_thoi_gian_tuoi_4='+che_do_hang_ngay_thoi_gian_tuoi_4)
            url_Update = 'http://mrduck.id.vn/Update_API_HaoDat_R_W?change_status=99&che_do_hang_ngay_xac_nhan_lan_1='+che_do_hang_ngay_xac_nhan_lan_1+'&che_do_hang_ngay_xac_nhan_lan_2='+che_do_hang_ngay_xac_nhan_lan_2+'&che_do_hang_ngay_xac_nhan_lan_3='+che_do_hang_ngay_xac_nhan_lan_3+'&che_do_hang_ngay_xac_nhan_lan_4='+che_do_hang_ngay_xac_nhan_lan_4+'&che_do_hang_ngay_dieu_khien_KV_1_1='+che_do_hang_ngay_dieu_khien_KV_1_1+'&che_do_hang_ngay_dieu_khien_KV_1_2='+che_do_hang_ngay_dieu_khien_KV_1_2+'&che_do_hang_ngay_dieu_khien_KV_1_3='+che_do_hang_ngay_dieu_khien_KV_1_3+'&che_do_hang_ngay_dieu_khien_KV_2_1='+che_do_hang_ngay_dieu_khien_KV_2_1+'&che_do_hang_ngay_dieu_khien_KV_2_2='+che_do_hang_ngay_dieu_khien_KV_2_2+'&che_do_hang_ngay_dieu_khien_KV_2_3='+che_do_hang_ngay_dieu_khien_KV_2_3+'&che_do_hang_ngay_dieu_khien_KV_3_1='+che_do_hang_ngay_dieu_khien_KV_3_1+'&che_do_hang_ngay_dieu_khien_KV_3_2='+che_do_hang_ngay_dieu_khien_KV_3_2+'&che_do_hang_ngay_dieu_khien_KV_3_3='+che_do_hang_ngay_dieu_khien_KV_3_3+'&che_do_hang_ngay_dieu_khien_KV_4_1='+che_do_hang_ngay_dieu_khien_KV_4_1+'&che_do_hang_ngay_dieu_khien_KV_4_2='+che_do_hang_ngay_dieu_khien_KV_4_2+'&che_do_hang_ngay_dieu_khien_KV_4_3='+che_do_hang_ngay_dieu_khien_KV_4_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_1='+che_do_hang_ngay_gio_bat_dau_tuoi_1+'&che_do_hang_ngay_gio_bat_dau_tuoi_2='+che_do_hang_ngay_gio_bat_dau_tuoi_2+'&che_do_hang_ngay_gio_bat_dau_tuoi_3='+che_do_hang_ngay_gio_bat_dau_tuoi_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_4='+che_do_hang_ngay_gio_bat_dau_tuoi_4+'&che_do_hang_ngay_phut_bat_dau_tuoi_1='+che_do_hang_ngay_phut_bat_dau_tuoi_1+'&che_do_hang_ngay_phut_bat_dau_tuoi_2='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_3='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_4='+che_do_hang_ngay_phut_bat_dau_tuoi_4+'&che_do_hang_ngay_thoi_gian_tuoi_1='+che_do_hang_ngay_thoi_gian_tuoi_1+'&che_do_hang_ngay_thoi_gian_tuoi_2='+che_do_hang_ngay_thoi_gian_tuoi_2+'&che_do_hang_ngay_thoi_gian_tuoi_3='+che_do_hang_ngay_thoi_gian_tuoi_3+'&che_do_hang_ngay_thoi_gian_tuoi_4='+che_do_hang_ngay_thoi_gian_tuoi_4
            # print(url_Update)
            requests.get(url_Update)
        url_R_W_HaoDat = 'http://mrduck.id.vn/Show_API_HaoDat_R_W?format=json'
        response_R_W_HaoDat = requests.get(url_R_W_HaoDat)
        parsed_data_R_W_HaoDat = json.loads(response_R_W_HaoDat.text)
        che_do_hang_ngay_xac_nhan_lan_1 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_xac_nhan_lan_1']
        che_do_hang_ngay_xac_nhan_lan_2 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_xac_nhan_lan_2']
        che_do_hang_ngay_xac_nhan_lan_3 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_xac_nhan_lan_3']
        che_do_hang_ngay_xac_nhan_lan_4 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_xac_nhan_lan_4']
        che_do_hang_ngay_dieu_khien_KV_1_1 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_1_1']
        che_do_hang_ngay_dieu_khien_KV_1_2 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_1_2']
        che_do_hang_ngay_dieu_khien_KV_1_3 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_1_3']
        che_do_hang_ngay_dieu_khien_KV_2_1 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_2_1']
        che_do_hang_ngay_dieu_khien_KV_2_2 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_2_2']
        che_do_hang_ngay_dieu_khien_KV_2_3 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_2_3']
        che_do_hang_ngay_dieu_khien_KV_3_1 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_3_1']
        che_do_hang_ngay_dieu_khien_KV_3_2 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_3_2']
        che_do_hang_ngay_dieu_khien_KV_3_3 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_3_3']
        che_do_hang_ngay_dieu_khien_KV_4_1 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_4_1']
        che_do_hang_ngay_dieu_khien_KV_4_2 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_4_2']
        che_do_hang_ngay_dieu_khien_KV_4_3 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_dieu_khien_KV_4_3']
        che_do_hang_ngay_thoi_gian_tuoi_1 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_thoi_gian_tuoi_1']
        che_do_hang_ngay_thoi_gian_tuoi_2 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_thoi_gian_tuoi_2']
        che_do_hang_ngay_thoi_gian_tuoi_3 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_thoi_gian_tuoi_3']
        che_do_hang_ngay_thoi_gian_tuoi_4 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_thoi_gian_tuoi_4']
        che_do_hang_ngay_gio_bat_dau_tuoi_1 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_gio_bat_dau_tuoi_1']
        che_do_hang_ngay_gio_bat_dau_tuoi_2 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_gio_bat_dau_tuoi_2']
        che_do_hang_ngay_gio_bat_dau_tuoi_3 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_gio_bat_dau_tuoi_3']
        che_do_hang_ngay_gio_bat_dau_tuoi_4 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_gio_bat_dau_tuoi_4']
        che_do_hang_ngay_phut_bat_dau_tuoi_1 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_phut_bat_dau_tuoi_1']
        che_do_hang_ngay_phut_bat_dau_tuoi_2 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_phut_bat_dau_tuoi_2']
        che_do_hang_ngay_phut_bat_dau_tuoi_3 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_phut_bat_dau_tuoi_3']
        che_do_hang_ngay_phut_bat_dau_tuoi_4 = parsed_data_R_W_HaoDat[0]['che_do_hang_ngay_phut_bat_dau_tuoi_4']
    elif user.username  == "KheCoc":
        print('Là Khe Cốc')
        if request.method == "POST":
            che_do_hang_ngay_xac_nhan_lan_1 = request.POST.get('day_1')
            if che_do_hang_ngay_xac_nhan_lan_1 == '1':
                che_do_hang_ngay_xac_nhan_lan_1 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_1 != '1':
                che_do_hang_ngay_xac_nhan_lan_1 = '0'
            che_do_hang_ngay_xac_nhan_lan_2 = request.POST.get('day_2')
            if che_do_hang_ngay_xac_nhan_lan_2 == '1':
                che_do_hang_ngay_xac_nhan_lan_2 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_2 != '1':
                che_do_hang_ngay_xac_nhan_lan_2 = '0'
            che_do_hang_ngay_xac_nhan_lan_3 = request.POST.get('day_3')
            if che_do_hang_ngay_xac_nhan_lan_3 == '1':
                che_do_hang_ngay_xac_nhan_lan_3 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_3 != '1':
                che_do_hang_ngay_xac_nhan_lan_3 = '0'
            che_do_hang_ngay_xac_nhan_lan_4 = request.POST.get('day_4')
            if che_do_hang_ngay_xac_nhan_lan_4 == '1':
                che_do_hang_ngay_xac_nhan_lan_4 = '1'
            elif che_do_hang_ngay_xac_nhan_lan_4 != '1':
                che_do_hang_ngay_xac_nhan_lan_4 = '0'
            area_1_1 = request.POST.get('area_1_1')
            print(area_1_1)
            if area_1_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_1_1 = '1'
            elif area_1_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_1_1 = '0'
            area_1_2 = request.POST.get('area_1_2')
            if area_1_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_1_2 = '1'
            elif area_1_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_1_2 = '0'
            area_1_3 = request.POST.get('area_1_3')
            if area_1_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_1_3 = '1'
            elif area_1_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_1_3 = '0'
            area_2_1 = request.POST.get('area_2_1')
            if area_2_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_2_1 = '1'
            elif area_2_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_2_1 = '0'
            area_2_2 = request.POST.get('area_2_2')
            if area_2_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_2_2 = '1'
            elif area_2_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_2_2 = '0'
            area_2_3 = request.POST.get('area_2_3')
            if area_2_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_2_3 = '1'
            elif area_2_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_2_3 = '0'
            area_3_1 = request.POST.get('area_3_1')
            if area_3_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_3_1 = '1'
            elif area_3_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_3_1 = '0'
            area_3_2 = request.POST.get('area_3_2')
            if area_3_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_3_2 = '1'
            elif area_3_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_3_2 = '0'
            area_3_3 = request.POST.get('area_3_3')
            if area_3_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_3_3 = '1'
            elif area_3_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_3_3 = '0'
            area_4_1 = request.POST.get('area_4_1')
            if area_4_1 == '1':
                che_do_hang_ngay_dieu_khien_KV_4_1 = '1'
            elif area_4_1 != '1':
                che_do_hang_ngay_dieu_khien_KV_4_1 = '0'
            area_4_2 = request.POST.get('area_4_2')
            if area_4_2 == '1':
                che_do_hang_ngay_dieu_khien_KV_4_2 = '1'
            elif area_4_2 != '1':
                che_do_hang_ngay_dieu_khien_KV_4_2 = '0'
            area_4_3 = request.POST.get('area_4_3')
            if area_4_3 == '1':
                che_do_hang_ngay_dieu_khien_KV_4_3 = '1'
            elif area_4_3 != '1':
                che_do_hang_ngay_dieu_khien_KV_4_3 = '0'
            
            che_do_hang_ngay_gio_bat_dau_tuoi_1 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_1')
            che_do_hang_ngay_gio_bat_dau_tuoi_2 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_2')
            che_do_hang_ngay_gio_bat_dau_tuoi_3 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_3')
            che_do_hang_ngay_gio_bat_dau_tuoi_4 = request.POST.get('che_do_hang_ngay_gio_bat_dau_tuoi_4')
            che_do_hang_ngay_phut_bat_dau_tuoi_1 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_1')
            che_do_hang_ngay_phut_bat_dau_tuoi_2 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_2')
            che_do_hang_ngay_phut_bat_dau_tuoi_3 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_3')
            che_do_hang_ngay_phut_bat_dau_tuoi_4 = request.POST.get('che_do_hang_ngay_phut_bat_dau_tuoi_4')
            che_do_hang_ngay_thoi_gian_tuoi_1 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_1')
            che_do_hang_ngay_thoi_gian_tuoi_2 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_2')
            che_do_hang_ngay_thoi_gian_tuoi_3 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_3')
            che_do_hang_ngay_thoi_gian_tuoi_4 = request.POST.get('che_do_hang_ngay_thoi_gian_tuoi_4')
            # print('che_do_hang_ngay_xac_nhan_lan_1='+che_do_hang_ngay_xac_nhan_lan_1+'&che_do_hang_ngay_xac_nhan_lan_2='+che_do_hang_ngay_xac_nhan_lan_2+'&che_do_hang_ngay_xac_nhan_lan_3='+che_do_hang_ngay_xac_nhan_lan_3+'&che_do_hang_ngay_xac_nhan_lan_4='+che_do_hang_ngay_xac_nhan_lan_4+'&che_do_hang_ngay_dieu_khien_KV_1_1='+che_do_hang_ngay_dieu_khien_KV_1_1+'&che_do_hang_ngay_dieu_khien_KV_1_2='+che_do_hang_ngay_dieu_khien_KV_1_2+'&che_do_hang_ngay_dieu_khien_KV_1_3='+che_do_hang_ngay_dieu_khien_KV_1_3+'&che_do_hang_ngay_dieu_khien_KV_2_1='+che_do_hang_ngay_dieu_khien_KV_2_1+'&che_do_hang_ngay_dieu_khien_KV_2_2='+che_do_hang_ngay_dieu_khien_KV_2_2+'&che_do_hang_ngay_dieu_khien_KV_2_3='+che_do_hang_ngay_dieu_khien_KV_2_3+'&che_do_hang_ngay_dieu_khien_KV_3_1='+che_do_hang_ngay_dieu_khien_KV_3_1+'&che_do_hang_ngay_dieu_khien_KV_3_2='+che_do_hang_ngay_dieu_khien_KV_3_2+'&che_do_hang_ngay_dieu_khien_KV_3_3='+che_do_hang_ngay_dieu_khien_KV_3_3+'&che_do_hang_ngay_dieu_khien_KV_4_1='+che_do_hang_ngay_dieu_khien_KV_4_1+'&che_do_hang_ngay_dieu_khien_KV_4_2='+che_do_hang_ngay_dieu_khien_KV_4_2+'&che_do_hang_ngay_dieu_khien_KV_4_3='+che_do_hang_ngay_dieu_khien_KV_4_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_1='+che_do_hang_ngay_gio_bat_dau_tuoi_1+'&che_do_hang_ngay_gio_bat_dau_tuoi_2='+che_do_hang_ngay_gio_bat_dau_tuoi_2+'&che_do_hang_ngay_gio_bat_dau_tuoi_3='+che_do_hang_ngay_gio_bat_dau_tuoi_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_4='+che_do_hang_ngay_gio_bat_dau_tuoi_4+'&che_do_hang_ngay_phut_bat_dau_tuoi_1='+che_do_hang_ngay_phut_bat_dau_tuoi_1+'&che_do_hang_ngay_phut_bat_dau_tuoi_2='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_3='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_4='+che_do_hang_ngay_phut_bat_dau_tuoi_4+'&che_do_hang_ngay_thoi_gian_tuoi_1='+che_do_hang_ngay_thoi_gian_tuoi_1+'&che_do_hang_ngay_thoi_gian_tuoi_2='+che_do_hang_ngay_thoi_gian_tuoi_2+'&che_do_hang_ngay_thoi_gian_tuoi_3='+che_do_hang_ngay_thoi_gian_tuoi_3+'&che_do_hang_ngay_thoi_gian_tuoi_4='+che_do_hang_ngay_thoi_gian_tuoi_4)
            url_Update = 'http://mrduck.id.vn/Update_API_KheCoc_R_W?change_status=99&che_do_hang_ngay_xac_nhan_lan_1='+che_do_hang_ngay_xac_nhan_lan_1+'&che_do_hang_ngay_xac_nhan_lan_2='+che_do_hang_ngay_xac_nhan_lan_2+'&che_do_hang_ngay_xac_nhan_lan_3='+che_do_hang_ngay_xac_nhan_lan_3+'&che_do_hang_ngay_xac_nhan_lan_4='+che_do_hang_ngay_xac_nhan_lan_4+'&che_do_hang_ngay_dieu_khien_KV_1_1='+che_do_hang_ngay_dieu_khien_KV_1_1+'&che_do_hang_ngay_dieu_khien_KV_1_2='+che_do_hang_ngay_dieu_khien_KV_1_2+'&che_do_hang_ngay_dieu_khien_KV_1_3='+che_do_hang_ngay_dieu_khien_KV_1_3+'&che_do_hang_ngay_dieu_khien_KV_2_1='+che_do_hang_ngay_dieu_khien_KV_2_1+'&che_do_hang_ngay_dieu_khien_KV_2_2='+che_do_hang_ngay_dieu_khien_KV_2_2+'&che_do_hang_ngay_dieu_khien_KV_2_3='+che_do_hang_ngay_dieu_khien_KV_2_3+'&che_do_hang_ngay_dieu_khien_KV_3_1='+che_do_hang_ngay_dieu_khien_KV_3_1+'&che_do_hang_ngay_dieu_khien_KV_3_2='+che_do_hang_ngay_dieu_khien_KV_3_2+'&che_do_hang_ngay_dieu_khien_KV_3_3='+che_do_hang_ngay_dieu_khien_KV_3_3+'&che_do_hang_ngay_dieu_khien_KV_4_1='+che_do_hang_ngay_dieu_khien_KV_4_1+'&che_do_hang_ngay_dieu_khien_KV_4_2='+che_do_hang_ngay_dieu_khien_KV_4_2+'&che_do_hang_ngay_dieu_khien_KV_4_3='+che_do_hang_ngay_dieu_khien_KV_4_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_1='+che_do_hang_ngay_gio_bat_dau_tuoi_1+'&che_do_hang_ngay_gio_bat_dau_tuoi_2='+che_do_hang_ngay_gio_bat_dau_tuoi_2+'&che_do_hang_ngay_gio_bat_dau_tuoi_3='+che_do_hang_ngay_gio_bat_dau_tuoi_3+'&che_do_hang_ngay_gio_bat_dau_tuoi_4='+che_do_hang_ngay_gio_bat_dau_tuoi_4+'&che_do_hang_ngay_phut_bat_dau_tuoi_1='+che_do_hang_ngay_phut_bat_dau_tuoi_1+'&che_do_hang_ngay_phut_bat_dau_tuoi_2='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_3='+che_do_hang_ngay_phut_bat_dau_tuoi_2+'&che_do_hang_ngay_phut_bat_dau_tuoi_4='+che_do_hang_ngay_phut_bat_dau_tuoi_4+'&che_do_hang_ngay_thoi_gian_tuoi_1='+che_do_hang_ngay_thoi_gian_tuoi_1+'&che_do_hang_ngay_thoi_gian_tuoi_2='+che_do_hang_ngay_thoi_gian_tuoi_2+'&che_do_hang_ngay_thoi_gian_tuoi_3='+che_do_hang_ngay_thoi_gian_tuoi_3+'&che_do_hang_ngay_thoi_gian_tuoi_4='+che_do_hang_ngay_thoi_gian_tuoi_4
            # print(url_Update)
            requests.get(url_Update)
        url_R_W_KheCoc = 'http://mrduck.id.vn/Show_API_KheCoc_R_W?format=json'
        response_R_W_KheCoc = requests.get(url_R_W_KheCoc)
        parsed_data_R_W_KheCoc = json.loads(response_R_W_KheCoc.text)
        che_do_hang_ngay_xac_nhan_lan_1 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_xac_nhan_lan_1']
        che_do_hang_ngay_xac_nhan_lan_2 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_xac_nhan_lan_2']
        che_do_hang_ngay_xac_nhan_lan_3 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_xac_nhan_lan_3']
        che_do_hang_ngay_xac_nhan_lan_4 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_xac_nhan_lan_4']
        che_do_hang_ngay_dieu_khien_KV_1_1 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_1_1']
        che_do_hang_ngay_dieu_khien_KV_1_2 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_1_2']
        che_do_hang_ngay_dieu_khien_KV_1_3 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_1_3']
        che_do_hang_ngay_dieu_khien_KV_2_1 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_2_1']
        che_do_hang_ngay_dieu_khien_KV_2_2 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_2_2']
        che_do_hang_ngay_dieu_khien_KV_2_3 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_2_3']
        che_do_hang_ngay_dieu_khien_KV_3_1 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_3_1']
        che_do_hang_ngay_dieu_khien_KV_3_2 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_3_2']
        che_do_hang_ngay_dieu_khien_KV_3_3 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_3_3']
        che_do_hang_ngay_dieu_khien_KV_4_1 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_4_1']
        che_do_hang_ngay_dieu_khien_KV_4_2 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_4_2']
        che_do_hang_ngay_dieu_khien_KV_4_3 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_dieu_khien_KV_4_3']
        che_do_hang_ngay_thoi_gian_tuoi_1 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_thoi_gian_tuoi_1']
        che_do_hang_ngay_thoi_gian_tuoi_2 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_thoi_gian_tuoi_2']
        che_do_hang_ngay_thoi_gian_tuoi_3 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_thoi_gian_tuoi_3']
        che_do_hang_ngay_thoi_gian_tuoi_4 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_thoi_gian_tuoi_4']
        che_do_hang_ngay_gio_bat_dau_tuoi_1 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_gio_bat_dau_tuoi_1']
        che_do_hang_ngay_gio_bat_dau_tuoi_2 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_gio_bat_dau_tuoi_2']
        che_do_hang_ngay_gio_bat_dau_tuoi_3 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_gio_bat_dau_tuoi_3']
        che_do_hang_ngay_gio_bat_dau_tuoi_4 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_gio_bat_dau_tuoi_4']
        che_do_hang_ngay_phut_bat_dau_tuoi_1 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_phut_bat_dau_tuoi_1']
        che_do_hang_ngay_phut_bat_dau_tuoi_2 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_phut_bat_dau_tuoi_2']
        che_do_hang_ngay_phut_bat_dau_tuoi_3 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_phut_bat_dau_tuoi_3']
        che_do_hang_ngay_phut_bat_dau_tuoi_4 = parsed_data_R_W_KheCoc[0]['che_do_hang_ngay_phut_bat_dau_tuoi_4']
    return render(request, "daily.html", {'filter':filtered_data, 'che_do_hang_ngay_xac_nhan_lan_1':che_do_hang_ngay_xac_nhan_lan_1, 'che_do_hang_ngay_xac_nhan_lan_2':che_do_hang_ngay_xac_nhan_lan_2, 'che_do_hang_ngay_xac_nhan_lan_3':che_do_hang_ngay_xac_nhan_lan_3, 'che_do_hang_ngay_xac_nhan_lan_4':che_do_hang_ngay_xac_nhan_lan_4, 'che_do_hang_ngay_dieu_khien_KV_1_1':che_do_hang_ngay_dieu_khien_KV_1_1, 'che_do_hang_ngay_dieu_khien_KV_1_2':che_do_hang_ngay_dieu_khien_KV_1_2, 'che_do_hang_ngay_dieu_khien_KV_1_3':che_do_hang_ngay_dieu_khien_KV_1_3, 'che_do_hang_ngay_dieu_khien_KV_2_1':che_do_hang_ngay_dieu_khien_KV_2_1, 'che_do_hang_ngay_dieu_khien_KV_2_2':che_do_hang_ngay_dieu_khien_KV_2_2, 'che_do_hang_ngay_dieu_khien_KV_2_3':che_do_hang_ngay_dieu_khien_KV_2_3, 'che_do_hang_ngay_dieu_khien_KV_3_1':che_do_hang_ngay_dieu_khien_KV_3_1, 'che_do_hang_ngay_dieu_khien_KV_3_2':che_do_hang_ngay_dieu_khien_KV_3_2, 'che_do_hang_ngay_dieu_khien_KV_3_3':che_do_hang_ngay_dieu_khien_KV_3_3, 'che_do_hang_ngay_dieu_khien_KV_4_1':che_do_hang_ngay_dieu_khien_KV_4_1, 'che_do_hang_ngay_dieu_khien_KV_4_2':che_do_hang_ngay_dieu_khien_KV_4_2, 'che_do_hang_ngay_dieu_khien_KV_4_3':che_do_hang_ngay_dieu_khien_KV_4_3, 'che_do_hang_ngay_thoi_gian_tuoi_1':che_do_hang_ngay_thoi_gian_tuoi_1, 'che_do_hang_ngay_thoi_gian_tuoi_2':che_do_hang_ngay_thoi_gian_tuoi_2, 'che_do_hang_ngay_thoi_gian_tuoi_3':che_do_hang_ngay_thoi_gian_tuoi_3, 'che_do_hang_ngay_thoi_gian_tuoi_4':che_do_hang_ngay_thoi_gian_tuoi_4, 'che_do_hang_ngay_gio_bat_dau_tuoi_1':che_do_hang_ngay_gio_bat_dau_tuoi_1, 'che_do_hang_ngay_gio_bat_dau_tuoi_2':che_do_hang_ngay_gio_bat_dau_tuoi_2, 'che_do_hang_ngay_gio_bat_dau_tuoi_3':che_do_hang_ngay_gio_bat_dau_tuoi_3, 'che_do_hang_ngay_gio_bat_dau_tuoi_4':che_do_hang_ngay_gio_bat_dau_tuoi_4, 'che_do_hang_ngay_phut_bat_dau_tuoi_1':che_do_hang_ngay_phut_bat_dau_tuoi_1, 'che_do_hang_ngay_phut_bat_dau_tuoi_2':che_do_hang_ngay_phut_bat_dau_tuoi_2, 'che_do_hang_ngay_phut_bat_dau_tuoi_3':che_do_hang_ngay_phut_bat_dau_tuoi_3, 'che_do_hang_ngay_phut_bat_dau_tuoi_4':che_do_hang_ngay_phut_bat_dau_tuoi_4})

@login_required
def pump_HTML(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    if user.username  == "ThaiMinh":
        print('Là Thái Minh')
        if request.method == "POST":
            pump_value = request.POST.get('pump')
            van_1 = request.POST.get('van_1')
            van_2 = request.POST.get('van_2')
            van_3 = request.POST.get('van_3')
            # print("Bơm: ", pump_value)
            # print("Van 1: ", van_1)
            # print("Van 2: ", van_2)
            # print("Van 3: ", van_3)
            if pump_value == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_ThaiMinh_R_W?change_status=1&che_do_bang_tay_dieu_khien_bom='+'1'
                requests.get(url_Update)
            elif pump_value == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_ThaiMinh_R_W?change_status=1&che_do_bang_tay_dieu_khien_bom='+'0'
                requests.get(url_Update)
            if van_1 == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_ThaiMinh_R_W?change_status=1&che_do_dieu_khien_van_KV_1='+'1'
                requests.get(url_Update)
            elif van_1 == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_ThaiMinh_R_W?change_status=1&che_do_dieu_khien_van_KV_1='+'0'
                requests.get(url_Update)
            if van_2 == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_ThaiMinh_R_W?change_status=1&che_do_dieu_khien_van_KV_2='+'1'
                requests.get(url_Update)
            elif van_2 == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_ThaiMinh_R_W?change_status=1&che_do_dieu_khien_van_KV_2='+'0'
                requests.get(url_Update)
            if van_3 == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_ThaiMinh_R_W?change_status=1&che_do_dieu_khien_van_KV_3='+'1'
                requests.get(url_Update)
            elif van_3 == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_ThaiMinh_R_W?change_status=1&che_do_dieu_khien_van_KV_3='+'0'
                requests.get(url_Update)
        
        url_R_W_ThaiMinh = 'http://mrduck.id.vn/Show_API_ThaiMinh_R_W?format=json'
        response_R_W_ThaiMinh = requests.get(url_R_W_ThaiMinh)
        parsed_data_R_W_ThaiMinh = json.loads(response_R_W_ThaiMinh.text)
        # print(parsed_data_R_W_ThaiMinh)
        che_do_bang_tay_dieu_khien_bom = parsed_data_R_W_ThaiMinh[0]['che_do_bang_tay_dieu_khien_bom']
        che_do_dieu_khien_van_KV_1 = parsed_data_R_W_ThaiMinh[0]['che_do_dieu_khien_van_KV_1']
        che_do_dieu_khien_van_KV_2 = parsed_data_R_W_ThaiMinh[0]['che_do_dieu_khien_van_KV_2']
        che_do_dieu_khien_van_KV_3 = parsed_data_R_W_ThaiMinh[0]['che_do_dieu_khien_van_KV_3']
    if user.username  == "HaoDat":
        print('Là Hảo Đạt')
        if request.method == "POST":
            pump_value = request.POST.get('pump')
            van_1 = request.POST.get('van_1')
            van_2 = request.POST.get('van_2')
            van_3 = request.POST.get('van_3')
            # print("Bơm: ", pump_value)
            # print("Van 1: ", van_1)
            # print("Van 2: ", van_2)
            # print("Van 3: ", van_3)
            if pump_value == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_HaoDat_R_W?change_status=1&che_do_bang_tay_dieu_khien_bom='+'1'
                requests.get(url_Update)
            elif pump_value == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_HaoDat_R_W?change_status=1&che_do_bang_tay_dieu_khien_bom='+'0'
                requests.get(url_Update)
            if van_1 == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_HaoDat_R_W?change_status=1&che_do_dieu_khien_van_KV_1='+'1'
                requests.get(url_Update)
            elif van_1 == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_HaoDat_R_W?change_status=1&che_do_dieu_khien_van_KV_1='+'0'
                requests.get(url_Update)
            if van_2 == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_HaoDat_R_W?change_status=1&che_do_dieu_khien_van_KV_2='+'1'
                requests.get(url_Update)
            elif van_2 == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_HaoDat_R_W?change_status=1&che_do_dieu_khien_van_KV_2='+'0'
                requests.get(url_Update)
            if van_3 == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_HaoDat_R_W?change_status=1&che_do_dieu_khien_van_KV_3='+'1'
                requests.get(url_Update)
            elif van_3 == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_HaoDat_R_W?change_status=1&che_do_dieu_khien_van_KV_3='+'0'
                requests.get(url_Update)
        url_R_W_HaoDat = 'http://mrduck.id.vn/Show_API_HaoDat_R_W?format=json'
        response_R_W_HaoDat = requests.get(url_R_W_HaoDat)
        parsed_data_R_W_HaoDat = json.loads(response_R_W_HaoDat.text)
        # print(parsed_data_R_W_ThaiMinh)
        che_do_bang_tay_dieu_khien_bom = parsed_data_R_W_HaoDat[0]['che_do_bang_tay_dieu_khien_bom']
        che_do_dieu_khien_van_KV_1 = parsed_data_R_W_HaoDat[0]['che_do_dieu_khien_van_KV_1']
        che_do_dieu_khien_van_KV_2 = parsed_data_R_W_HaoDat[0]['che_do_dieu_khien_van_KV_2']
        che_do_dieu_khien_van_KV_3 = parsed_data_R_W_HaoDat[0]['che_do_dieu_khien_van_KV_3']
    if user.username  == "KheCoc":
        print('Là Khe Cốc')
        if request.method == "POST":
            pump_value = request.POST.get('pump')
            van_1 = request.POST.get('van_1')
            van_2 = request.POST.get('van_2')
            van_3 = request.POST.get('van_3')
            # print("Bơm: ", pump_value)
            # print("Van 1: ", van_1)
            # print("Van 2: ", van_2)
            # print("Van 3: ", van_3)
            if pump_value == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_KheCoc_R_W?change_status=1&che_do_bang_tay_dieu_khien_bom='+'1'
                requests.get(url_Update)
            elif pump_value == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_KheCoc_R_W?change_status=1&che_do_bang_tay_dieu_khien_bom='+'0'
                requests.get(url_Update)
            if van_1 == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_KheCoc_R_W?change_status=1&che_do_dieu_khien_van_KV_1='+'1'
                requests.get(url_Update)
            elif van_1 == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_KheCoc_R_W?change_status=1&che_do_dieu_khien_van_KV_1='+'0'
                requests.get(url_Update)
            if van_2 == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_KheCoc_R_W?change_status=1&che_do_dieu_khien_van_KV_2='+'1'
                requests.get(url_Update)
            elif van_2 == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_KheCoc_R_W?change_status=1&che_do_dieu_khien_van_KV_2='+'0'
                requests.get(url_Update)
            if van_3 == 'on':
                url_Update = 'http://mrduck.id.vn/Update_API_KheCoc_R_W?change_status=1&che_do_dieu_khien_van_KV_3='+'1'
                requests.get(url_Update)
            elif van_3 == 'off':
                url_Update = 'http://mrduck.id.vn/Update_API_KheCoc_R_W?change_status=1&che_do_dieu_khien_van_KV_3='+'0'
                requests.get(url_Update)
        url_R_W_KheCoc = 'http://mrduck.id.vn/Show_API_KheCoc_R_W?format=json'
        response_R_W_KheCoc = requests.get(url_R_W_KheCoc)
        parsed_data_R_W_KheCoc = json.loads(response_R_W_KheCoc.text)
        che_do_bang_tay_dieu_khien_bom = parsed_data_R_W_KheCoc[0]['che_do_bang_tay_dieu_khien_bom']
        che_do_dieu_khien_van_KV_1 = parsed_data_R_W_KheCoc[0]['che_do_dieu_khien_van_KV_1']
        che_do_dieu_khien_van_KV_2 = parsed_data_R_W_KheCoc[0]['che_do_dieu_khien_van_KV_2']
        che_do_dieu_khien_van_KV_3 = parsed_data_R_W_KheCoc[0]['che_do_dieu_khien_van_KV_3']
    return render(request, "pump.html", {'filter':filtered_data, 'che_do_bang_tay_dieu_khien_bom':che_do_bang_tay_dieu_khien_bom, 'che_do_dieu_khien_van_KV_1':che_do_dieu_khien_van_KV_1, 'che_do_dieu_khien_van_KV_2':che_do_dieu_khien_van_KV_2, 'che_do_dieu_khien_van_KV_3':che_do_dieu_khien_van_KV_3})

@login_required
def user_HTML(request):
    user_role = request.user
    finter = Manager_User.objects.all().filter(user=user_role)
    for x in finter:
        if x.Area == "Quản trị":
            print("Là quản trị hoặc giám sát")
            if request.method == "POST":
                name = request.POST.get("name")
                password = request.POST.get("password")
                Household_name = request.POST.get("Household")
                area = request.POST.get("area")
                if name and password and Household_name and area:
                    create_user = User.objects.create_user(name, password=password)
                    create_user.is_staff = True
                    create_user.save()
                    create_info = Manager_User(user=name, password=password, Household_Name=Household_name, Area=area)
                    create_info.save()
                return redirect('/user_HTML/')
            user_ = Manager_User.objects.all()
            user = request.user  # Lấy giá trị user từ request
            filtered_data = Manager_User.objects.all().filter(user=user)
            return render(request, "user.html", {'user_list': user_, 'filter':filtered_data})
        else:
            print("Không phải")
            return render(request, '404.html')


@login_required
def manager_Delete(request, id):
    if request.method == 'POST':
        id_delete = Manager_User.objects.get(pk=id)
        model_id = Manager_User.objects.get(id=id_delete.id)
        authenticate_id = User.objects.filter(username=model_id.user)
        id_delete.delete()
        authenticate_id.delete()
        return redirect('/user_HTML/')

@login_required
def manager_Update(request, id):
    if request.method == "POST":
        edit_name = request.POST.get('edit_name')
        edit_Household = request.POST.get('edit_Household')
        edit_area = request.POST.get('edit_area')
        print("======================================")
        id_delete = Manager_User.objects.get(pk=id)
        model_id = Manager_User.objects.get(id=id_delete.id)
        print(f"Password hiện tại là: {model_id.password}, use: {model_id.user}")
        edit_password = model_id.password
        print("======================================")
        if edit_name and edit_Household:
            authenticate_id = User.objects.filter(username=model_id.user)
            id_delete.delete()
            authenticate_id.delete()
            create_user = User.objects.create_user(edit_name, password=edit_password)
            create_user.is_staff = True
            create_user.save()
            save_info = Manager_User(id=id, user=edit_name, password=edit_password, Household_Name=edit_Household, Area=edit_area)
            save_info.save()
            return redirect('/user_HTML/')
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(userName=user)
    return render(request, 'user.html', {'filter':filtered_data})

@login_required
def location_HTML(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    return render(request, "location.html", {'filter':filtered_data})

def Logout(request):
    logout(request)
    messages.error(request, "Bạn đã đăng xuất")
    return redirect('/')

def Show_HaoDat_info(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    area = 'HaoDat'
    return render(request, "HaoDat/info_HaoDat.html", {'filter_area':area, 'filter':filtered_data})

def Show_HaoDat_stats(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    area = 'HaoDat'
    return render(request, "HaoDat/Stats_HaoDat.html", {'filter_area':area, 'filter':filtered_data})

def Show_ThaiMinh_info(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    area = 'ThaiMinh'
    url = 'http://mrduck.id.vn/Show_API_ThaiMinh_read?format=json'
    response = requests.get(url)
    parsed_data = json.loads(response.text)
    nhiet_do_dat = parsed_data[0]['nhiet_do_dat']
    do_am_dat = parsed_data[0]['do_am_dat']
    do_ph = parsed_data[0]['do_ph']
    trang_thai_van_khu_vuc_1 = parsed_data[0]['trang_thai_van_khu_vuc_1']
    trang_thai_van_khu_vuc_2 = parsed_data[0]['trang_thai_van_khu_vuc_2']
    trang_thai_van_khu_vuc_3 = parsed_data[0]['trang_thai_van_khu_vuc_3']
    trang_thai_bom = parsed_data[0]['trang_thai_bom']
    url_R_W = 'http://mrduck.id.vn/Show_API_ThaiMinh_R_W?format=json'
    response_R_W = requests.get(url_R_W)
    parsed_data_R_W = json.loads(response_R_W.text)
    che_do_hoat_dong = parsed_data_R_W[0]['che_do_hoat_dong']
    return render(request, "ThaiMinh/info_ThaiMinh.html", {'filter_area':area, 'filter':filtered_data, 'nhiet_do_dat': nhiet_do_dat, 'do_am_dat': do_am_dat, 'do_ph': do_ph, 'trang_thai_van_khu_vuc_1':trang_thai_van_khu_vuc_1, 'trang_thai_van_khu_vuc_2':trang_thai_van_khu_vuc_2, 'trang_thai_van_khu_vuc_3':trang_thai_van_khu_vuc_3, 'trang_thai_bom':trang_thai_bom, 'che_do_hoat_dong':che_do_hoat_dong})

def Show_ThaiMinh_status(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    area = 'ThaiMinh'

    return render(request, "ThaiMinh/Stats_ThaiMinh.html", {'filter_area':area, 'filter':filtered_data})

def Show_KheCoc_info(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    area = 'KheCoc'
    return render(request, "KheCoc/info_KheCoc.html", {'filter_area':area, 'filter':filtered_data})

def Show_KheCoc_status(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    area = 'KheCoc'
    
    return render(request, "KheCoc/Stats_KheCoc.html", {'filter_area':area, 'filter':filtered_data})

def get_data(request):
    user_role = request.user
    print(user_role)

    if user_role.username  == "ThaiMinh":
        print('Là Thái Minh')
        url = 'http://mrduck.id.vn/Show_API_ThaiMinh_read?format=json'
        response = requests.get(url)

        parsed_data = json.loads(response.text)
        nhiet_do_dat = parsed_data[0]['nhiet_do_dat']
        do_am_dat = parsed_data[0]['do_am_dat']
        do_ph = parsed_data[0]['do_ph']
        trang_thai_van_khu_vuc_1 = parsed_data[0]['trang_thai_van_khu_vuc_1']
        trang_thai_van_khu_vuc_2 = parsed_data[0]['trang_thai_van_khu_vuc_2']
        trang_thai_van_khu_vuc_3 = parsed_data[0]['trang_thai_van_khu_vuc_3']
        trang_thai_bom = parsed_data[0]['trang_thai_bom']

        url_R_W = 'http://mrduck.id.vn/Show_API_ThaiMinh_R_W?format=json'
        response_R_W = requests.get(url_R_W)
        parsed_data_R_W = json.loads(response_R_W.text)
        che_do_hoat_dong = parsed_data_R_W[0]['che_do_hoat_dong']
        return nhiet_do_dat, do_am_dat, do_ph, trang_thai_van_khu_vuc_1, trang_thai_van_khu_vuc_2, trang_thai_van_khu_vuc_3, trang_thai_bom, che_do_hoat_dong

    elif user_role.username  == "KheCoc":
        print('Là Khe Cốc')
        url = 'http://mrduck.id.vn/Show_API_KheCoc_read?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            parsed_data = json.loads(response.text)
            nhiet_do_dat = parsed_data[0]['nhiet_do_dat']
            do_am_dat = parsed_data[0]['do_am_dat']
            do_ph = parsed_data[0]['do_ph']
            return nhiet_do_dat, do_am_dat, do_ph

    elif user_role.username  == "HaoDat":
        print('Là Hảo Đạt')
        url = 'http://mrduck.id.vn/Show_API_HaoDat_read?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            parsed_data = json.loads(response.text)
            nhiet_do_dat = parsed_data[0]['nhiet_do_dat']
            do_am_dat = parsed_data[0]['do_am_dat']
            do_ph = parsed_data[0]['do_ph']
            return nhiet_do_dat, do_am_dat, do_ph

    # Move the return statement outside the loop
    return None, None, None, None, None, None, None, None
