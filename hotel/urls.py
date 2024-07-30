from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from hotel_booking import urls

urlpatterns = [
    path("api/", include(urls)),
    path("admin/", admin.site.urls),
]

urlpatterns+=staticfiles_urlpatterns()

