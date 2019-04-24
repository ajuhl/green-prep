
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('meal/', include('mealbuilder.urls')),
    path('grocerylist/', include('grocerylist.urls')),
    path('profile/', include('userprofile.urls')),
    path('', views.index, name='index'),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
