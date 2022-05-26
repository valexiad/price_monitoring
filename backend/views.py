from django.shortcuts import render
from django.http import HttpResponse
from backend.models import TrackItemHeader, TrackItemComponents
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
def index(request):
    return HttpResponse('Welcome! This site is under construction, come back later...')


class TrackItemHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackItemHeader
        fields = ('name', 'description', 'user')


class TrackItemHeaderViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    queryset = TrackItemHeader.objects.all()
    serializer_class = TrackItemHeaderSerializer

    def get_queryset(self):
        user = self.request.user
        return TrackItemHeader.objects.filter(user=user)

    def list_queryset(self):
        user = self.request.user
        return TrackItemHeader.objects.filter(user=user)

    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]


