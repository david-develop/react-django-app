from core.serializers import UserSerializer

def my_jwt_response_handler(token, user=None, request=None):
    """custom JWT response payload handler which includes the user's serialized data"""
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
}
