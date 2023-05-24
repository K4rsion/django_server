class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response=self.get_response(request)
        
        if hasattr(request, 'path') and 'plot' in request.path:
            response['Cache-Control'] = "no-store,  no-cache, must-revalidate"
            return response
        if hasattr(request, 'path') and 'login' in request.path:
            response['Cache-Control'] = "no-store"
            return response
        if hasattr(request, 'path') and 'text' in request.path:
            response['Cache-Control'] = "public, max-age=600"
            return response
        if hasattr(request, 'path') and 'about' in request.path:
            response['Cache-Control'] = "no-store,  no-cache"
            return response
        if hasattr(request, 'path') and '' in request.path:
            response['Cache-Control'] = "no-store,  no-cache"
            return response
        