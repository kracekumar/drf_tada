from django.conf.urls import patterns, include, url

from django.contrib import admin

from user.views import (UserDetailApiView, UserListApiView,
                        UserChangePasswordApiView)
from todo.views import (TodoBucketListApiView)


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drsf_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/(?P<pk>[0-9]+)/change_password/$', UserChangePasswordApiView.as_view(), name='change-password'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailApiView.as_view(), name='user-detail'),
    url(r'^todo_bucket/$', TodoBucketListApiView.as_view(),
        name='todo-bucket-list'),
)
