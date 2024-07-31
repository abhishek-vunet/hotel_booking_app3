from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("api/v1/customer/", include("customer.urls")),
    path("api/v1/hotels/", include("hotels.urls")),
    path("api/v1/booking/", include("booking.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns+=staticfiles_urlpatterns()

