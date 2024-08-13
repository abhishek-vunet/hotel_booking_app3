from django.urls import path
from .views import (HotelGetApiView,
                    HotelAddApiView,
                    HotelGetByIdApiView,
                    HotelUpdateByIdApiView,
                    HotelDeleteByIdApiView,
                    SearchHotelByNameApiView,

                    ReviewGetApiView,
                    ReviewAddApiView,
                    ReviewGetByIdApiView,
                    ReviewUpdateByIdApiView,
                    ReviewDeleteByIdApiView,

                    RoomGetApiView,
                    RoomAddApiView,
                    RoomGetByIdApiView,
                    RoomUpdateByIdApiView,
                    RoomDeleteByIdApiView,

                    AmenitiesGetApiView,
                    AmenitiesAddApiView,
                    AmenitiesGetByIdApiView,
                    AmenitiesUpdateByIdApiView,
                    AmenitiesDeleteByIdApiView,

                    
                )

urlpatterns = [
    path('getAllHotels', HotelGetApiView.as_view()),
    path('addHotel', HotelAddApiView.as_view()),
    path('getHotelById/<int:id>', HotelGetByIdApiView.as_view()),
    path('updateHotelById/<int:id>', HotelUpdateByIdApiView.as_view()),
    path('deleteHotelById/<int:id>', HotelDeleteByIdApiView.as_view()),
    path('searchHotelByName/<str:name>', SearchHotelByNameApiView.as_view()),

    path('getAllRooms', RoomGetApiView.as_view()),
    path('addRoom', RoomAddApiView.as_view()),
    path('getRoomById/<int:id>', RoomGetByIdApiView.as_view()),
    path('updateRoomById/<int:id>', RoomUpdateByIdApiView.as_view()),
    path('deleteRoomById/<int:id>', RoomDeleteByIdApiView.as_view()),
    
    path('getAllReviews', ReviewGetApiView.as_view()),
    path('addReview', ReviewAddApiView.as_view()),
    path('getReviewById/<int:id>', ReviewGetByIdApiView.as_view()),
    path('updateReviewById/<int:id>', ReviewUpdateByIdApiView.as_view()),
    path('deleteReviewById/<int:id>', ReviewDeleteByIdApiView.as_view()),

    path('getAllAmenities', AmenitiesGetApiView.as_view()),
    path('addAmenity', AmenitiesAddApiView.as_view()),
    path('getAmenityById/<int:id>', AmenitiesGetByIdApiView.as_view()),
    path('updateAmenityById/<int:id>', AmenitiesUpdateByIdApiView.as_view()),
    path('deleteAmenityById/<int:id>', AmenitiesDeleteByIdApiView.as_view()),
]