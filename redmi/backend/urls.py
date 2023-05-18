from django.urls import path
from .views import SignupView, LoginView, LogoutView

urlpatterns = [
    path('backend/signup/', SignupView.as_view(), name='signup'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
]
