from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Manager_User, API_ThaiMinh, API_HaoDat, API_KheCoc

from rest_framework import status
from .serializers import Data_Serializer_HaoDat, Data_Serializer_KheCoc, Data_Serializer_ThaiMinh
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
from django.http import JsonResponse


# Create your views here.

@api_view(['GET'])
def Create_API_HaoDat(request):
    serializer = Data_Serializer_HaoDat(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Tạo mới API Hảo Đạt thành công!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, tạo API thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def Show_API_HaoDat(request):
    data = API_HaoDat.objects.all()
    serializer = Data_Serializer_HaoDat(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def Update_API_Hao_Dat(request):
    data = get_object_or_404(API_HaoDat, pk=1)
    serializer = Data_Serializer_HaoDat(data, data=request.GET.dict())

    if serializer.is_valid():
        serializer.save()
        url = 'http://127.0.0.1:8000/Show_API_HaoDat?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse({
                'message': json.dumps(response.json()) 
            }, status=status.HTTP_200_OK)

        return JsonResponse({'message': 'Cập nhật thành công!'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Lỗi, cập nhật không thành công!'}, status=status.HTTP_400_BAD_REQUEST)

# ===========================================================
@api_view(['GET'])
def Create_API_KheCoc(request):
    serializer = Data_Serializer_KheCoc(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Tạo mới API Khê Cốc thành công!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, tạo API thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def Show_API_KheCoc(request):
    data = API_KheCoc.objects.all()
    serializer = Data_Serializer_KheCoc(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def Update_API_KheCoc(request):
    data = get_object_or_404(API_KheCoc, pk=1)
    serializer = Data_Serializer_KheCoc(data, data=request.GET.dict())

    if serializer.is_valid():
        serializer.save()
        url = 'http://127.0.0.1:8000/Show_API_KheCoc?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse({
                'message': json.dumps(response.json()) 
            }, status=status.HTTP_200_OK)

        return JsonResponse({'message': 'Cập nhật thành công!'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Lỗi, cập nhật không thành công!'}, status=status.HTTP_400_BAD_REQUEST)

# ===========================================================
@api_view(['GET'])
def Create_API_ThaiMinh(request):
    serializer = Data_Serializer_ThaiMinh(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Tạo mới API Thái Minh thành công!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, tạo API thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def Show_API_ThaiMinh(request):
    data = API_ThaiMinh.objects.all()
    serializer = Data_Serializer_ThaiMinh(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def Update_API_ThaiMinh(request):
    data = get_object_or_404(API_ThaiMinh, pk=1)
    serializer = Data_Serializer_ThaiMinh(data, data=request.GET.dict())

    if serializer.is_valid():
        serializer.save()
        url = 'http://127.0.0.1:8000/Show_API_ThaiMinh?format=json'
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
    return render(request, "info.html", {'filter':filtered_data})

@login_required
def home_HTML(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    return render(request, "home.html", {'filter':filtered_data})

@login_required
def daily_HTML(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    return render(request, "daily.html", {'filter':filtered_data})

@login_required
def pump_HTML(request):
    user = request.user  # Lấy giá trị user từ request
    filtered_data = Manager_User.objects.all().filter(user=user)
    return render(request, "pump.html", {'filter':filtered_data})

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
    return render(request, "ThaiMinh/info_ThaiMinh.html", {'filter_area':area, 'filter':filtered_data})

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
