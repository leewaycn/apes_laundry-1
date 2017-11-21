# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as userlogin, logout as userlogout
import json

from users.models import User
from aliyun_msg.models import PhoneCaptcha
from aliyun_msg.aliyun_msg import send_phoneCode, verify_phoneCode
from .models import CustomerAddress


# Create your views here.
USER_TYPE = 1 #1 表示用户端
USER_LABEL = "customer_"
@login_required()
def index(request):
    # print request.user.username
    username = request.user.username
    phone = username[9:]
    return render(request,'customers/index.html',{"user_phone":phone})
@csrf_exempt
def code(request):
    if request.method == "POST":
        result = {}
        phone = request.POST.get("phone")
        print("customer_phone:"), phone
        ret = send_phoneCode(phone=phone, type=USER_TYPE)
        if ret['code'] == 'OK':
            result["result"] = "success"  # 1成功
            result["code"] = ret['code']
        else:
            result["result"] = "fail"  # 1成功
            result["errMsg"] = ret['errMsg']
        print "res:{0}".format(result)
        res = json.dumps(result)
        return HttpResponse(res.decode("unicode-escape"), content_type="application/json")

@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, 'customers/log.html')
    if request.method == "POST":
        result = {}
        phone = request.POST.get("phone")
        username = USER_LABEL + phone
        code = request.POST.get("code")
        vc = verify_phoneCode(phone=phone, code=code, type=USER_TYPE)
        if vc == 1:
            try:
                user = User.objects.get(username=username);
                userlogin(request,user)
                result["result"] = "success"
            except User.DoesNotExist:
                # result["errMsg"] = "手机号未注册用户，用户不存在，请先注册！"
                # result["result"] = "fail"
                user = User(username=username);
                user.set_password(username)
                user.is_active = 1
                user.save()
                userlogin(request, user)
                result["result"] = "success"
        elif vc == 2:
            result["errMsg"] = "验证码过期，请重新发送验证码！"
            result["result"] = "fail"
        elif vc == 3:
            result["errMsg"] = "验证码错误，请输入正确的验证码！"
            result["result"] = "fail"
        elif vc == 4:
            result["errMsg"] = "请先发送验证！"
            result["result"] = "fail"
        res = json.dumps(result)
        return HttpResponse(res.decode("unicode-escape"), content_type="application/json")

@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, 'customers/register.html')
    if request.method == "POST":
        result = {}
        phone = request.POST.get("phone")
        username = USER_LABEL + phone
        code = request.POST.get("code")
        vc = verify_phoneCode(phone=phone, code=code, type=USER_TYPE)
        if vc == 1:
            try:
                user = User.objects.get(username=username);
                userlogin(request,user)
                result["result"] = "success"
            except User.DoesNotExist:
                # result["errMsg"] = "手机号未注册用户，用户不存在，请先注册！"
                # result["result"] = "fail"
                user = User(username=username);
                user.set_password(username)
                user.is_active = 1
                user.save()
                userlogin(request, user)
                result["result"] = "success"
        elif vc == 2:
            result["errMsg"] = "验证码过期，请重新发送验证码！"
            result["result"] = "fail"
        elif vc == 3:
            result["errMsg"] = "验证码错误，请输入正确的验证码！"
            result["result"] = "fail"
        elif vc == 4:
            result["errMsg"] = "请先发送验证！"
            result["result"] = "fail"
        res = json.dumps(result)
        return HttpResponse(res.decode("unicode-escape"), content_type="application/json")

@csrf_exempt
def logout(request):
    userlogout(request)
    return HttpResponseRedirect('/customers/login/')

@csrf_exempt
def test(request):
    return render(request,"customers/test.html")

@csrf_exempt
def address(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address  = request.POST.get('address')
        door_number = request.POST.get('door_number')
        # sex = request.POST.get('sex')
        sex = True
        try:
            customer_address = CustomerAddress.objects.filter(user_id=request.user.id)[0]
            customer_address.name = name
            customer_address.phone = phone
            customer_address.door_number = door_number
            customer_address.sex = sex
            customer_address.save()
        except IndexError:
            customer_address = CustomerAddress(name=name, phone=phone, address=address, door_number=door_number, sex=sex)
            customer_address.user_id = request.user.id
            customer_address.save()

        return HttpResponseRedirect('/customer/index/')
    if request.method == "GET":
        user_id = request.user.id
        l =  CustomerAddress.objects.filter(user_id=user_id)
        res = {}
        if len(l)> 0 :
            cuAddress = l[0]
            res['result'] = "sucess"
            res['name'] = cuAddress.name
            res['phone'] = cuAddress.phone
            res['address'] = cuAddress.address
            res['door_number'] = cuAddress.door_number
        res = json.dumps(res)
        return render(request, 'customers/address.html',{"res":res})
@csrf_exempt
def customer_address(request):
    user_id = request.user.id
    cuAddress = CustomerAddress.objects.filter(user_id=user_id)[0]
    res = {}
    res['result'] = "sucess"
    res['name'] = cuAddress.name
    res['phone'] = cuAddress.phone
    res['address'] =cuAddress.address
    res['door_number'] = cuAddress.door_number
    res = json.dumps(res)
    print res.decode("unicode-escape")
    return HttpResponse(res.decode("unicode-escape"), content_type="application/json")