
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('meals/', include('mealbuilder.urls')),
    path('grocerylist/', include('grocerylist.urls')),
    path('profile/', include('userprofile.urls')),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

