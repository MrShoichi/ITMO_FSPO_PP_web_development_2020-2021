from django.urls import path
from .views import *

urlpatterns = [
    path('CarOwner/<int:id>/', detail),
    path('СarOwner/', car_owners),
    path('CarOwner/list', CarOwnersList.as_view()),
    path('CarList/', CarList.as_view()),
    path('car/<int:pk>/', CarDetail.as_view()),
    path('car/list/', ListCar.as_view()),
    path('CarOwner/add', register_student),
    path('car/<int:pk>/update/', CarUpdate.as_view()),
    path('car/create/', CarCreate.as_view()),
    path('car/<int:pk>/delete/', CarDelete.as_view()),
]