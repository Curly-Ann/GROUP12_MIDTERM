from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
import json
from .services import register_user, authenticate_user

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = register_user(data)
            return JsonResponse({"success": True, "message": "User registered successfully", "user": user.username})
        except ValidationError as e:
            return JsonResponse({"success": False, "error": str(e)})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid request method"})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = authenticate_user(data)
            return JsonResponse({"success": True, "message": "Login successful", "user": user.username})
        except ValidationError as e:
            return JsonResponse({"success": False, "error": str(e)})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid request method"})
