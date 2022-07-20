from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bookrecommender/', include('bookrecommender.urls')),
    path('admin/', admin.site.urls),
]