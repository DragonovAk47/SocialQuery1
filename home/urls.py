from django.conf.urls import url
from home.views  import HomeView,change_friend,post_create,friends_list
urlpatterns=[
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',change_friend,name="change_friend"),
    url(r'^post_create/',post_create,name="post_create"),
    url(r'^friends/(?P<pk>\d+)/',friends_list,name="friends_list"),

]