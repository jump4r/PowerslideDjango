from django.conf.urls import url
from . import views

app_name = 'beatmaps'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^submit/', views.submit, name="submit"),
    url(r'^handlesubmit/', views.handle_submit, name="handle_submit"),
    url(r'^(?P<submission_id>[0-9]+)/$', views.details, name='detail')
]   