from django.urls import path
from .views import (BookingGetApiView,
                    # BookingAddApiView,
                    BookingGetByIdApiView,
                    BookingUpdateByIdApiView,
                    BookingDeleteByIdApiView,

                    PendingBookingGetApiView,
                    PendingBookingAddApiView,
                    PendingBookingGetByIdApiView,
                    PendingBookingUpdateByIdApiView,
                    PendingBookingDeleteByIdApiView,

                    Check_inGetApiView,
                    Check_inAddApiView,
                    Check_inGetByIdApiView,
                    Check_inUpdateByIdApiView,
                    Check_inDeleteByIdApiView,

                    Check_outGetApiView,
                    Check_outAddApiView,
                    Check_outGetByIdApiView,
                    Check_outUpdateByIdApiView,
                    Check_outDeleteByIdApiView,
                )

urlpatterns = [

    path('getAllPendingBookings', PendingBookingGetApiView.as_view()),
    path('addPendingBooking', PendingBookingAddApiView.as_view()),
    path('getPendingBookingById/<int:id>', PendingBookingGetByIdApiView.as_view()),
    path('updatePendihotelsngBookingById/<int:id>', PendingBookingUpdateByIdApiView.as_view()),
    path('deletePendingBookingById/<int:id>', PendingBookingDeleteByIdApiView.as_view()),

    path('getAllBookings', BookingGetApiView.as_view()),
    # path('addBooking', BookingAddApiView.as_view()),
    path('getBookingById/<int:id>', BookingGetByIdApiView.as_view()),
    path('updateBookingById/<int:id>', BookingUpdateByIdApiView.as_view()),
    path('deleteBookingById/<int:id>', BookingDeleteByIdApiView.as_view()),
    
    path('getAllCheck_in', Check_inGetApiView.as_view()),
    path('addCheck_in', Check_inAddApiView.as_view()),
    path('getCheck_inById/<int:id>', Check_inGetByIdApiView.as_view()),
    path('updateCheck_inById/<int:id>', Check_inUpdateByIdApiView.as_view()),
    path('deleteCheck_inById/<int:id>', Check_inDeleteByIdApiView.as_view()),

    path('getAllCheck_out', Check_outGetApiView.as_view()),
    path('addCheck_out', Check_outAddApiView.as_view()),
    path('getCheck_outById/<int:id>', Check_outGetByIdApiView.as_view()),
    path('updateCheck_outById/<int:id>', Check_outUpdateByIdApiView.as_view()),
    path('deleteCheck_outById/<int:id>', Check_outDeleteByIdApiView.as_view()),
]