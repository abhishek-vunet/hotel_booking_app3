from django.urls import path
from .views import (HotelGetApiView,
                    HotelAddApiView,
                    HotelGetByIdApiView,
                    HotelUpdateByIdApiView,
                    HotelDeleteByIdApiView,
                    ReviewGetApiView,
                    ReviewAddApiView,
                    ReviewGetByIdApiView,
                    ReviewUpdateByIdApiView,
                    ReviewDeleteByIdApiView
                )

urlpatterns = [
    path('getAllHotels', HotelGetApiView.as_view()),
    path('addHotel', HotelAddApiView.as_view()),
    path('getHotelById/<int:id>', HotelGetByIdApiView.as_view()),
    path('updateHotelById/<int:id>', HotelUpdateByIdApiView.as_view()),
    path('deleteHotelById/<int:id>', HotelDeleteByIdApiView.as_view()),
    
    path('getAllReviews', ReviewGetApiView.as_view()),
    path('addReview', ReviewAddApiView.as_view()),
    path('getReviewById/<int:id>', ReviewGetByIdApiView.as_view()),
    path('updateReviewById/<int:id>', ReviewUpdateByIdApiView.as_view()),
    path('deleteReviewById/<int:id>', ReviewDeleteByIdApiView.as_view()),
]