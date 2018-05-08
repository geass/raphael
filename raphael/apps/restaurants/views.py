from .models import Restaurants
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import permissions, routers, serializers, viewsets
from .serializers import RestaurantsSerializer


class RestaurantsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer