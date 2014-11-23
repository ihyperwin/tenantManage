#!/usr/bin/python
#coding=utf-8

from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from forms import LoginForm,ChangePasswordForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from utils import get_datatables_records
from django.contrib.auth.decorators import login_required
from models import SEX_CHOICES,Tenant
from django.utils import jslex
from forms import TenantForm
from django.core.serializers.json import json
from django.utils.cache import add_never_cache_headers
import traceback
from django.core.serializers import json
import datetime

@login_required
def index(request):
    username = request.user.username
    userId = request.user.id

    return render_to_response('tenant/tenant.html',{
            "title":'租客管理',
            'username':username,'userId':userId},context_instance = RequestContext(request))

@login_required
def get_tenants_list(request):
    
    #过滤状态为1，且userId为当前登陆人的，所有的租客
    tenants = Tenant.objects.filter(status='1',user_id=request.user.id)

    columnIndexNameMap = {
        0:'id',                   
        1:'name',
        2:'sex',
        3:'mobile_number',
        4:'house_number',
        5:'rent_date',
        6:'remind_date',
        7:'rent_money',
    }
    
    columnNameIndexMap = dict([[v,k] for k,v in columnIndexNameMap.items()])

    
    try:
        tenantsData,sEcho,iTotalRecords,iTotalDisplayRecords,sColumns = get_datatables_records(request, tenants, columnIndexNameMap, extrafilters = {'sex':SEX_CHOICES,}) 
    except Exception,e:
        traceback.print_stack()
        print e
        tenantsData,sEcho,iTotalRecords,iTotalDisplayRecords,sColumns = [],1,0,0,','.join(columnIndexNameMap.values())
    
    for i in tenantsData:
        i[columnNameIndexMap['sex']] = dict(SEX_CHOICES)[i[columnNameIndexMap['sex']]]

    response_dict = {}
    response_dict.update({'aaData':tenantsData})
    response_dict.update({
        'sEcho': sEcho, 
        'iTotalRecords': iTotalRecords, 
        'iTotalDisplayRecords':iTotalDisplayRecords, 
        'sColumns':sColumns})

    response =  HttpResponse(json.json.dumps(response_dict))

    #阻止缓存
    add_never_cache_headers(response)
    return response

@login_required
def addtenant(request):
    username = request.user.username
    userId = request.user.id
    
    if request.method == "POST":
        form = TenantForm(data = request.POST,userId = userId )
        if form.is_valid():
            form.save()
            success = True
            successinfo = "添加"
            return render_to_response('tenant/tenant.html',{
                "title":'租客管理',
                'form':form,
                'successinfo':successinfo,
                'success':success,
                'username':username},context_instance = RequestContext(request))
        else:
            return render_to_response('tenant/tenant.html',{
                "title":'租客管理',
                'form':form,
                'username':username},context_instance = RequestContext(request))

    return HttpResponseRedirect('/manage/tenant/')

@login_required
def edittenant(request):
    username = request.user.username

    if request.method == "POST":
        try:
            tenant_id = request.POST.get('id')
            try:
                tenant = Tenant.objects.get(id = tenant_id)
                tenant.mobile_number = request.POST.get('editMobileNumber')
                tenant.rent_money =request.POST.get('editRentMoney')
                tenant.remind_date = request.POST.get('editRemindDate')
                tenant.done_date = datetime.datetime.now()
                tenant.save()
                success = True
                successinfo = "修改"
                return render_to_response('tenant/tenant.html',{
                     "title":'租客管理',
                      #'form':form,
                     'successinfo':successinfo,
                     'success':success,
                     'username':username},context_instance = RequestContext(request))
            except Tenant.DoesNotExist:
                traceback.print_stack()
        except Exception:
            traceback.print_stack()
    return HttpResponseRedirect('/manage/tenant/')

@login_required
def deletetenant(request):
    username = request.user.username
    
    if request.method == "POST":
        try:
            tenant_id = request.POST.get('id')
            try:
                deltenant = Tenant.objects.get(id = tenant_id)
                deltenant.status='0'
                deltenant.done_date = datetime.datetime.now()
                deltenant.save()
                success = True
                successinfo = "删除"
                return render_to_response('tenant/tenant.html',{
                    "title":'租客管理',
                    'successinfo':successinfo,
                    'success':success,
                    'username':username},context_instance = RequestContext(request))
            except Tenant.DoesNotExist:
                traceback.print_stack()
        except Exception:
            traceback.print_stack()
        
    return HttpResponseRedirect('/manage/tenant/')

@login_required
def tenantprofile(request):
    tenant_id = request.GET.get('id')
    tenant = Tenant.objects.get(id = tenant_id)
    result_dic={}
    result_dic["id"]=tenant.id
    result_dic["name"]=tenant.name
    result_dic["sex"]=tenant.sex
    result_dic["mobileNumber"]=tenant.mobile_number
    result_dic["community"]=tenant.community
    result_dic["unit"]=tenant.unit
    result_dic["houseNumber"]=tenant.house_number
    result_dic["rentMoney"]=tenant.rent_money
    result_dic["rentDate"]=tenant.rent_date
    result_dic["remindDate"]=tenant.remind_date

    response =  HttpResponse(json.json.dumps(result_dic,cls=json.DjangoJSONEncoder))

    #阻止缓存
    add_never_cache_headers(response)
    return response
