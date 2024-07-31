from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("api/customer/", include("customer.urls")),
    path("api/hotels/", include("hotels.urls")),
    path("api/booking/", include("booking.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns+=staticfiles_urlpatterns()

