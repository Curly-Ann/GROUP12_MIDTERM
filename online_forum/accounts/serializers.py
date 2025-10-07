from django.core.exceptions import ValidationError

def validate_registration(data):
    username = data.get('username')
    password = data.get('password')

    if not username:
        raise ValidationError("Username is required.")
    if not password or len(password) < 6:
        raise ValidationError("Password must be at least 6 characters long.")

def validate_login(data):
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        raise ValidationError("Username and password are required.")
