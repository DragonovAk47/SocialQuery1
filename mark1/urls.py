
from django.contrib import admin
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$',views.login_redirect,name='login_redirect'),
    url('admin/', admin.site.urls),
    url(r'^home/', include(('home.urls', 'home'), namespace="home")),
    url(r'^iron2/',include(('iron2.urls', 'iron2'),namespace="iron2")),
    url(r'^blog/',include(('blog.urls', 'blog'),namespace="blog")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
