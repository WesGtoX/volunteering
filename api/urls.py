from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from volunteers.views import VoluntaryViewSet
from actions.views import ActionViewSet

router = routers.DefaultRouter()
router.register(r'volunteers', VoluntaryViewSet)
router.register(r'actions', ActionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
