"""price_monitoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backend.user.models import User
from rest_framework.schemas import get_schema_view
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
import backend.views
from backend.user.viewsets import UserViewSet
from backend.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
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
    http_method_names = ['get', 'post']
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter]
    authentication_classes = [SessionAuthentication]
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id=user.id)

    def list_queryset(self):
        user = self.request.user
        return User.objects.filter(user=user)

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('users/(?P<user_id>\d+)/track-items', backend.views.TrackItemHeaderViewSet, basename='track-items')

# AUTHENTICATION
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
# router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', backend.views.index, name="index"),
    path('', include(router.urls)),
    # path('users', UserViewSet.as_view({'get': 'list'}), name='users'),
    # path('users/<int:user_id>/track-', backend.views.TrackItemHeaderViewSet.as_view({'get': 'list'}), name='track-items'),
    # path('openapi/', get_schema_view(
    #     title="Price Monitoring Service", public=True,
    # ), name='openapi-schema'),
    # path('docs/', TemplateView.as_view(
    #     template_name='documentation.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger-ui'),
    # YOUR PATTERNS
    path('schema/', SpectacularAPIView.as_view(permission_classes=[AllowAny]), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]



