#coding=utf-8
'''
Created on 2014年10月28日

@author: Administrator
'''
from django.db import models
#from django.contrib import admin


SEX_CHOICES = (
    ('0','男'),
    ('1','女'),
)

class Tenant(models.Model):
    name = models.CharField(u"姓名",max_length = 256)
    sex = models.CharField(u'性别',choices = SEX_CHOICES,max_length = 1)
    mobile_number = models.CharField(u'手机号码',max_length = 11)
    community = models.CharField(u'小区',max_length = 512)
    unit = models.CharField(u'单元',max_length = 256)
    house_number = models.CharField(u'房号',max_length = 6)
    rent_money = models.IntegerField(u'租金',max_length = 6)
    rent_date = models.DateField(u'出租时间')
    remind_date = models.DateField(u'提醒时间')
    status = models.CharField(u'状态', max_length = 1);
    user_id = models.CharField(u'用户ID',max_length = 11)
    done_date=models.DateTimeField(u'更新时间')
 
    
    class Meta:
        db_table = u"tenant"
        verbose_name_plural = '租客'
    
    
    


    
        
    

    