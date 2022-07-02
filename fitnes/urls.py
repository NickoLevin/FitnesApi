from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse
def trigger_error(request):
    division_by_zero = 1/0
    return HttpResponse('error')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('sentry-debug/', trigger_error),
]
 