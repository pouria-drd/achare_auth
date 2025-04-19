import os
from dotenv import load_dotenv
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static

# Loads the variables from the .env file into the environment
load_dotenv()

router = routers.DefaultRouter()


base_url: str = os.getenv("BASE_URL", "")

urlpatterns = [
    path(base_url, include(router.urls)),
    # main admin
    path(base_url + os.getenv("ADMIN_URL", "admin/"), admin.site.urls),
    # api urls
    path(base_url + "accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.index_title = "Achare"
admin.site.site_header = "Achare Admin"
admin.site.site_title = "Achare"
