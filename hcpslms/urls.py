from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('add-issue/', include('mainapp.urls')),
    path('add-book/', include('mainapp.urls')),
    path('add-publication/', include('mainapp.urls')),
    path('add-author/', include('mainapp.urls')),
    path('view-author/', include('mainapp.urls')),
    path('view-issue/', include('mainapp.urls')),
    path('view-publication/', include('mainapp.urls')),
    path('view-book/', include('mainapp.urls')), 
]
