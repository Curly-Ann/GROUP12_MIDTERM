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
