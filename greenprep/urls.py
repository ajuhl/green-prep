
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('meals/', include('mealbuilder.urls')),
    path('grocerylist/', include('grocerylist.urls')),
    path('profile/', include('userprofile.urls')),
    path('mealcalendar/', include('mealcalendar.urls')),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
