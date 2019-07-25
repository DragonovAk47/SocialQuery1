from django.conf.urls import url
from django.urls import reverse
from . import views
from iron2.forms import LoginForm

from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete
urlpatterns=[

    url(r'^login/$',login,{'template_name':'iron2/login.html','authentication_form':LoginForm},name='login'),
    url(r'^logout/$',logout,{'template_name':'iron2/logout.html'},name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'^pdf_files/(?P<id>\d+)/$',views.pdf_view,name='pdf_files'),
    url(r'^upload/$',views.model_form_upload,name='upload'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^userprofile/$',views.UserProfileView,name='UserProfileView'),
    url(r'^profile/(?P<pk>\d+)/$',views.profile,name='profile_with_pk'),
    url(r'^edit_form/',views.edit_form,name='edit_form'),
    url(r'^change_password/',views.change_password,name='change_password'),
    url(r'^reset_password/',password_reset,
        {'template_name':'iron2/reset_password.html','post_reset_redirect':'iron2:password_reset_done','email_template_name':'iron2/reset_password_email.html'},
        name='reset_password'),
    url(r'^reset_password_done/',password_reset_done,name='password_reset_done'),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',password_reset_confirm,name='password_reset_confirm'),
    url(r'^reset_password_complete/',password_reset_complete,name='password_reset_complete'),

]