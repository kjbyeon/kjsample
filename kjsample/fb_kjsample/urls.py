from django.conf.urls import include, url
from .views import KjSampleView

urlpatterns = [
    url(r'^702ded6f187504536957fe4f0338c60a6aef3eea97d86bb340/?$', KjSampleView.as_view()),
]
