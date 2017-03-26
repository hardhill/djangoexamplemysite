# filename urls
# author hardh
# datetime 27.03.2017 - 0:23
from django.conf.urls import url

from mysite import views

urlpatterns=[
    url(r'^$',views.post_list, name='post_list')
]