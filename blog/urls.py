from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^blog_create/',views.blog_create,name="blog_create"),
    url(r'^blog_list/',views.blog_list,name="blog_list"),
    url(r'^myblog/',views.myblog,name="myblog"),
    url(r'^blog_full/(?P<pk>\d+)/$',views.blog_full,name="blog_full"),
    url(r'^blog_edit/(?P<pk>\d+)/$',views.blog_edit,name="blog_edit"),
]