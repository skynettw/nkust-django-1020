from django.contrib import admin
from django.urls import path
from mainsite.views import homepage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
]
