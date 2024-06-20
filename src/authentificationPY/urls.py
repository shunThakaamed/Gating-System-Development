# your-repo/src/authentication/urls.py

from django.urls import path
from .views import RegisterView, VerifyNFTView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-nft/', VerifyNFTView.as_view(), name='verify_nft'),
]
