from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def test(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': request.build_absolute_uri(reverse('api-users')),  # Fixed users path
    })

@api_view(['GET'])
def api_users(request, format=None):
    return Response({
        'login': request.build_absolute_uri(reverse('login')),
        'logout': request.build_absolute_uri(reverse('logout')),
        'signup': request.build_absolute_uri(reverse('signup')),
        'verify': request.build_absolute_uri(reverse('verify')),
        'new_verify': request.build_absolute_uri(reverse('new-verify')),
        'update_user': request.build_absolute_uri(reverse('update-user')),
        'update_user_photo': request.build_absolute_uri(reverse('update-user-photo')),
        'forgot_password': request.build_absolute_uri(reverse('forgot-password')),
        'reset_password': request.build_absolute_uri(reverse('reset-password')),
    })