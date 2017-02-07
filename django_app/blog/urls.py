from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^post$', views.post_list, name='post_list'),
    url(r'^post/detail/(?P<post_id>[0-9]+)/', views.post_detail, name='post_detail'),
]