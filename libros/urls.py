from django.conf.urls import url
from . import views

app_name = "libros"

urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard")
]