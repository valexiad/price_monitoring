from django.shortcuts import render
from django.http import HttpResponse
from backend.models import TrackItemHeader, TrackItemComponents
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.core.exceptions import PermissionDenied
from backend.user.models import User


# Create your views here.
def index(request):
    return HttpResponse('Welcome! This site is under construction, come back later...')


class TrackItemHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackItemHeader
        fields = ('name', 'description', 'user')
        read_only_fields = ['user']

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        validated_data['user'] = User.objects.get(id=user_id)
        return super().create(validated_data)


class TrackItemHeaderViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a track item instance.

    list:
        Return all track items of the user, ordered by most recently joined.

    create:
        Create a new track item .

    delete:
        Remove an existing track item.

    partial_update:
        Update one or more fields on an existing track item.

    update:
        Update a track item.
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
        if 'user_id' in self.kwargs:
            if self.request.user.id != int(self.kwargs['user_id']):
                raise PermissionDenied()
        
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


