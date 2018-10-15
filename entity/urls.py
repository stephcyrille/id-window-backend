from django.conf.urls import url 

from .views import EntitiesList, EntityPartialUpdateCni, EntityPartialUpdateStatus, EntityCorrespondQueryList, EntityDistributionQueryList, EntityDetail, sendSms


urlpatterns = [
    url(r'^entities/$', EntitiesList.as_view()),
    url(r'^entities/update/cni/(?P<pk>\d+)/$', EntityPartialUpdateCni.as_view()),
    url(r'^entities/update/status/(?P<pk>\d+)/$', EntityPartialUpdateStatus.as_view()),
    url(r'^entities/correspond/q/(?P<search>)$', EntityCorrespondQueryList.as_view()),
    url(r'^entities/distribution/q/(?P<search>)$', EntityDistributionQueryList.as_view()),
    url(r'^entities/detail/$', EntityDetail.as_view()),

    url(r'^entities/update/sendSms/(?P<id>\d+)/$', sendSms),
]