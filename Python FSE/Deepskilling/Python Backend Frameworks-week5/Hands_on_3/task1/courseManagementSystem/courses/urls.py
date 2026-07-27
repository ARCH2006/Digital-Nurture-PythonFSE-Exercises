# from django.urls import path
# from .views import hello_view

# urlpatterns = [
#     path("hello/",hello_view),
# ]
from django.urls import path
from .views import courseView,CourseDetailView

urlpatterns = [path("courses/",courseView.as_view()),
               path("courses/<int:pk>/",CourseDetailView.as_view()),
               ]