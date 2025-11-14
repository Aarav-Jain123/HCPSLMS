# from .views import *


# class TrackURLMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # This runs before the view is called
#         url_path = request.path  # Full URL user is visiting

#         # Optional: Only track GET requests to avoid logging forms, API posts, etc.
#         if request.method == "GET":
#             if "add" in url_path:
#                 if 'book' in url_path:
#                     add_new_content(request, 'book')
#                 elif 'author' in url_path:
#                     add_new_content(request, 'author')
#                 elif 'publication' in url_path:
#                     add_new_content(request, 'publication')
#                 elif 'issue' in url_path:
#                     add_new_content(request, 'issue')               

#         response = self.get_response(request)  # Call the view
#         return response