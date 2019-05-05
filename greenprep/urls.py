
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from greenprep import views as core_views
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('meal/', include('mealbuilder.urls')),
    path('grocerylist/', include('grocerylist.urls')),
    path('profile/', include('userprofile.urls')),
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
