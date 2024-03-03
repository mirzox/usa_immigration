from django.urls import path, include

from .views import ServiceView, AnotherServiceView, FamilyServiceView

urlpatterns = [
    path('service/', ServiceView.as_view()),
    path('another_service/', AnotherServiceView.as_view()),
    path('family_service/', FamilyServiceView.as_view())
]