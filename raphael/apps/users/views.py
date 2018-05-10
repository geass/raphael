from rest_framework import permissions, routers, serializers, viewsets
from django.contrib.auth import get_user_model
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from .serializers import UsersSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UsersSerializer(user, context={'request': request}).data
    }

class CreateUsersViewSet(viewsets.ModelViewSet):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsersSerializer