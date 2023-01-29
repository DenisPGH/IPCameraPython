
from django.contrib import admin
from django.urls import path

from Camera.views import openCam, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stream/',IndexView.as_view(), name='index'),
    path('', openCam, name='cam'),
]
