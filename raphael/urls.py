from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

## Viewsets
from raphael.apps.restaurants.views import RestaurantsViewSet
from raphael.apps.users.views import CreateUsersViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantsViewSet)
router.register(r'user/register', CreateUsersViewSet, base_name='inoutreports')

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
]
