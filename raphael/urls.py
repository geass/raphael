from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from raphael.apps.restaurants.views import RestaurantsViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantsViewSet)

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
