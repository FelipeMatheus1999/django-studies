# Django
from django.contrib import admin
from django.urls import path, include

# Project
from apps.account.urls import router as account_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(account_router.urls))
]
