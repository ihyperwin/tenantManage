from django.conf.urls import include, url,patterns
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'tenantManage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'engine.views.index'),

    url(r'^grappelli/',include('grappelli.urls')),
   # url(r'^user/', include('engine.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^favicon.ico$', 'django.shortcuts.redirect', {'url': '/static/images/favicon.png'}),

    url(r'^accounts/login/$', 'engine.account.userlogin', name="userlogin"),
    url(r'^accounts/logout/$',  'django.contrib.auth.views.logout',
                                {'next_page': '/accounts/login/'},name="userlogout"),           
    url(r'^accounts/changepassword/$', 'engine.account.changepassword', name="changepassword"),
    
    url(r'^manage/tenant/$', 'engine.tenant.index',name="managetenant"),
    url(r'^manage/addtenant/$', 'engine.tenant.addtenant',name="addtenant"),
    url(r'^manage/edittenant/$', 'engine.tenant.edittenant',name="edittenant"),
    url(r'^manage/deletetenant/$', 'engine.tenant.deletetenant',name="deletetenant"),
    #tenant ajax
    url(r'^ajax/get_tenants_list/$', 'engine.tenant.get_tenants_list',name="get_tenants_list"),
    url(r'^ajax/tenantprofile/$', 'engine.tenant.tenantprofile',name="tenantprofile"),
]

if  settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve',{'document_root':settings.STATIC_ROOT}),
    )

