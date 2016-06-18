from django.conf.urls import url
import views

urlpatterns=[
  url(r'^shudata/$',views.provider_list),
  url(r'^shudata/(?P<pk>[0-9]+)/$',views.provider_detail),
]