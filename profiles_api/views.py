from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers, models, permissions



class UserProfileViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar perfiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class CourseViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar cursos """
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class FatherFamilyViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar padres de familia cuando el usuario esta logeado """
    serializer_class = serializers.FatherFamilySerializer
    queryset = models.FatherFamily.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RegistrationViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar matriculas cuando el usuario esta logeado """
    serializer_class = serializers.RegistrationSerializer
    queryset = models.Registration.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class UserLoginApiView(ObtainAuthToken):
    """ Crea tokens de autenticacion de usuario """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Maneja el crear, leer y actualizar el profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus, 
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """ Setear el perfil de usuario para el usuario que esta logeado """
        serializer.save(user_profile=self.request.user)