from django.urls import path

from pagination_filter.views import StudentViews

urlpatterns = [
     path('getstudents/',StudentViews.as_view(), name='students-api'),
]