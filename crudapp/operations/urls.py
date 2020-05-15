from django.urls import path

from .views import get_cars, show_cars, post_car, CarOperations

urlpatterns = [
    path('cars', get_cars),
    path('show/', show_cars),
    path('car/', post_car),
    path('car/<int:pk>', CarOperations.as_view()),
]
