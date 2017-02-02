from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^(?P<my_args>\d+)/$', TemplateView.as_view(template_name="article/detail.html"), name='detail'),
]