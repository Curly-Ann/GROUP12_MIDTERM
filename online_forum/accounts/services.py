from .models import User
from .serializers import validate_registration
from django.core.exceptions import ValidationError

def register_user(data):
    validate_registration(data)
    username = data['username']
    password = data['password']
    role = data.get('role', 'member')

    if User.objects.filter(username=username).exists():
        raise ValidationError("Username already exists.")

    user = User(username=username, role=role)
    user.set_password(password)
    user.save()
    return user

def authenticate_user(data):
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        raise ValidationError("Username and password are required.")

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise ValidationError("Invalid username or password.")

    if not user.check_password(password):
        raise ValidationError("Invalid username or password.")

    return user
