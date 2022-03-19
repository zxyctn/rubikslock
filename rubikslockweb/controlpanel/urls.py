from django.urls import path
from . import views

app_name = "controlpanel"

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name="upload"),
    path('new', views.new, name="new"),
    path('set', views.set_password, name="set"),
]