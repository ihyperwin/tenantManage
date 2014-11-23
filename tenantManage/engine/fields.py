#!/usr/bin/python
#coding=utf-8

from django.forms.fields import CharField
from validators import username,password,tenantName

class UsernameField(CharField):
    default_error_messages = {
        'invalid':u'3-12位,由字母数字下划线组成,首字母为字母',
        'required':u'用户名必须要填',
        'max_length':u'管理员用户名至多为12位',
        'min_length':u'管理员用户名至少为3位'
    }
    default_validators = [username]

    def clean(self,value):
        value = self.to_python(value).strip()
        return super(UsernameField, self).clean(value)


class PasswordField(CharField):
    default_error_messages = {
        'invalid':u'密码由字母数字下划线组成的字符串，最少为6位',
        'required':u'密码必须要填(由字母数字下划线组成的字符串，最少为6位)',
        'max_length':u'密码至多为12位',
        'min_length':u'密码至少为6位'
    }
    default_validators = [password]
    
class TenantNameField(CharField):
    default_error_messages = {
        'invalid':u'姓名必须是2-6个汉字',
        'required':u'姓名必须要填（2-6个汉字）',
    }
    default_validators = [tenantName]

    def clean(self,value):
        value = self.to_python(value).strip()
        return super(TenantNameField, self).clean(value)

