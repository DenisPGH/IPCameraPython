
from django.contrib import admin
from django.urls import path, include

from Camera.views import  openCam

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stream/', IndexView.as_view(), name='index'),
    path('', openCam, name='cam'),
]
