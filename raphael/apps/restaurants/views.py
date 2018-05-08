from .models import Restaurants
from rest_framework import viewsets
from .serializers import RestaurantsSerializer


class RestaurantsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer