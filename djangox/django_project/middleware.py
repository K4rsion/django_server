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

        #для авторизованных пользователей
        if request.user.is_authenticated:
            if hasattr(request, 'path') and 'about' in request.path:
                response['Cache-Control'] = "private, max-age=600"
            elif hasattr(request, 'path') and '' in request.path:
                response['Cache-Control'] = "private, no-transform, max-age=600"
            return response
        
        # для неавторизованных пользователей
        elif request.user.is_anonymous:
            if hasattr(request, 'path') and 'about' in request.path:
                response['Cache-Control'] = "public, max-age=600"
            elif hasattr(request, 'path') and '' in request.path:
                response['Cache-Control'] = "public, no-transform, max-age=600"
            return response
        