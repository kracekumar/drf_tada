from django.conf.urls import patterns, include, url

from django.contrib import admin

from user.views import (UserDetailApiView, UserListApiView,
                        UserChangePasswordApiView)
from todo.views import (TodoBucketListApiView, TodoBucketDetailApiView)
from task.views import (TaskListApiView, TaskDetailApiView, NoteListApiView,
                        NoteDetailApiView)

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
    url(r'^todo_bucket/(?P<todo_bucket_pk>[0-9]+)/$', TodoBucketDetailApiView.as_view(),
        name='todo-bucket-detail'),
    url(r'^todo_bucket/(?P<todo_bucket_pk>[0-9]+)/tasks/$',
        TaskListApiView.as_view(),
        name='task-list'),
    url(r'^todo_bucket/(?P<todo_bucket_pk>[0-9]+)/tasks/(?P<task_pk>[0-9]+)/$',
        TaskDetailApiView.as_view(),
        name='task-detail'),
    url(r'^todo_bucket/(?P<todo_bucket_pk>[0-9]+)/tasks/(?P<task_pk>[0-9]+)/notes/$',
        NoteListApiView.as_view(),
        name='note-list'),
    url(r'^todo_bucket/(?P<todo_bucket_pk>[0-9]+)/tasks/(?P<task_pk>[0-9]+)/notes/(?P<note_pk>[0-9]+)/$',
        NoteDetailApiView.as_view(),
        name='note-detail'),

)
