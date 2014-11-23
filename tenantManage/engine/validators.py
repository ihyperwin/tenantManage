#!/usr/bin/python
#coding=utf-8

import re
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

username_re = re.compile(r'^[a-z]+$')
username = RegexValidator(username_re,u'请正确输入用户名，为姓名拼音，全部小写','invalid')

password_re = re.compile(r'^[\w]+?$')
password = RegexValidator(password_re,u'密码由字母数字下划线组成的字符串','invalid')

TenantName_re = re.compile(r'^[\u4e00-\u9fa5]{2,6}$')


class TenantNameValidator(object):
    message = u'租客姓名必须是2-6个汉字'
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self,value):
        if not all([True if i >= u'\u4e00' and i <= u'\u9fa5' else False for i in value]):
            raise ValidationError(self.message, code=self.code)

tenantName = TenantNameValidator()



