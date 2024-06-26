from django.urls import path,include
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users', views.CreateUserView.as_view(), name='createuser')

]