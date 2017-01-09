from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^record-activity/$', views.AnalyticsActivityCreateView.as_view(), name='record-activity'),
]
