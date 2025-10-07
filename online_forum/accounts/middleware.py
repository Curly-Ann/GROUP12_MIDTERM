from django.http import JsonResponse

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.protected_paths = [
            '/thread/',
            '/post/',
        ]

    def __call__(self, request):
        if any(request.path.startswith(path) for path in self.protected_paths):
            if not request.user.is_authenticated:
                return JsonResponse({"success": False, "error": "Authentication required"}, status=401)

        return self.get_response(request)
