#!/usr/bin/python
#coding=utf-8

from django import forms
from fields import UsernameField,PasswordField,TenantNameField
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from models import Tenant,SEX_CHOICES
import traceback
import datetime

class LoginForm(forms.Form):
    username = UsernameField(required=True,max_length=12,min_length=3)
    password = PasswordField(required=True,max_length=12,min_length=6)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            #如果成功返回对应的User对象，否则返回None(只是判断此用户是否存在，不判断是否is_active或者is_staff)
            if self.user_cache is None:
                raise forms.ValidationError(u"您输入的用户名或密码不正确!")
            elif not self.user_cache.is_active or not self.user_cache.is_staff:
                raise forms.ValidationError(u"您输入的用户名或密码不正确!")
            else:
                login(self.request,self.user_cache)
        return self.cleaned_data
        
    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache

class ChangePasswordForm(forms.Form):
    """
        A form used to change the password of a user in the admin interface.
    """
    newpassword = PasswordField(required=True,max_length=12,min_length=6)
    renewpassword = PasswordField(required=True,max_length=12,min_length=6)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_password2(self):
        newpassword = self.cleaned_data.get('newpassword')
        renewpassword = self.cleaned_data.get('renewpassword')
        if newpassword and renewpassword:
            if newpassword != renewpassword:
                raise forms.ValidationError(u"此处必须输入和上栏密码相同的内容")
        raise forms.ValidationError(u"此处必须输入和上栏密码相同的内容")
        return renewpassword

    def save(self, commit=True):
        """
        Saves the new password.
        """
        self.user.set_password(self.cleaned_data["newpassword"])
        if commit:
            self.user.save()
        return self.user


class TenantForm(forms.Form):
    name = TenantNameField(required=True,max_length=6,min_length=2)
    sex = forms.ChoiceField(required=True,choices=SEX_CHOICES,error_messages={'invalid':u'请您正确选择下拉框'})
    mobileNumber = forms.CharField(required=True,max_length=11,min_length=1,error_messages={'invalid':u'请输入正确手机号'})
    community = forms.CharField(required=True,max_length=512,min_length=1,error_messages={'invalid':u'请输入正确的小区名'})  
    unit = forms.CharField(required=True,max_length=256,min_length=1,error_messages={'invalid':u'请输入正确的单元名'}) 
    houseNumber = forms.CharField(required=True,max_length=11,min_length=1,error_messages={'invalid':u'请输入正确的房间号'}) 
    rentMoney = forms.CharField(required=True,max_length=11,min_length=1,error_messages={'invalid':u'请输入正确的租金'})  
    rentDate = forms.DateField(required=True,input_formats=['%Y-%m-%d',],error_messages={'invalid':u'请输入正确格式的入住日期'})
    remindDate = forms.DateField(required=True,input_formats=['%Y-%m-%d',],error_messages={'invalid':u'请输入正确格式的提醒日期'})

    
    
    def __init__(self, userId=None, *args, **kwargs):
        self.userId = userId
        super(TenantForm, self).__init__(*args, **kwargs)


    def clean_tenant_id(self):
        if self.get_id():
            try:
                Tenant.objects.get(id = self.get_id())
            except Tenant.DoesNotExist:
                raise forms.ValidationError(u"请不要非法提交数据")
            return self.get_id()
        return self.get_id()
    
    
    def get_id(self):
        return self.cleaned_data['id']
    
    
    def save(self,commit=True):
        tenant = Tenant(rent_date=self.cleaned_data['rentDate'],\
        remind_date=self.cleaned_data['remindDate'],rent_money=self.cleaned_data['rentMoney'],\
        house_number=self.cleaned_data['houseNumber'],unit=self.cleaned_data['unit'],\
        community=self.cleaned_data['community'],mobile_number=self.cleaned_data['mobileNumber'],\
        sex=self.cleaned_data['sex'],name=self.cleaned_data['name'])
        tenant.status = '1'
        tenant.user_id=self.userId
        tenant.done_date=datetime.datetime.now()
        if commit:
            tenant.save()
    

        

        
        