from django.conf.urls import url
from . import views

urlpatterns = [
    # post_list 뷰를 ^$ URL에 할당
    # name='post_list는 URL에 이름 할당
    url(r'^$', views.post_list, name='post_list'),
]
