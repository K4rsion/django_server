class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response=self.get_response(request)
        
        if hasattr(request, 'path') and not any(text in request.path for text in ['text1', 'text2', 'text3']):
            response['Cache-Control'] = "no-store;no-cache;must-revalidate"
            return response
        if hasattr(request, 'path') and any(text in request.path for text in ['text1', 'text2', 'text3']) and (request.user.is_authenticated or request.user.is_anonymous):
            response['Cache-Control'] = "public;max-age=600"
            return response
        