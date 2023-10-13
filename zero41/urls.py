from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PhoneView.as_view(), name='home'),
    path('create/', CreatePhone.as_view(), name='create'),
    path('xiaomi/', XiaomiView.as_view(), name='xiaomi'),
]