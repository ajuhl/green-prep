
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mealbuilder/', include('mealbuilder.urls')),
    path('grocerylist/', include('grocerylist.urls')),
    path('userprofile/', include('userprofile.urls')),
]
