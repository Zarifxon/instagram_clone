from django.urls import path
from .views import (CreateUserView,
                    VerifyAPIView,
                    GetNewVerification,
                    ChangeUserInformationView,
                    ChangeUserPhotoView,


                    )

urlpatterns = [
    path('signup/', CreateUserView.as_view()),
    path('verify/', VerifyAPIView.as_view()),
    #28
    path('new-verify/', GetNewVerification.as_view()),
    # 29
    path('change-user/', ChangeUserInformationView.as_view()),
    #30
    path('change-user-photo/', ChangeUserPhotoView.as_view()),
]