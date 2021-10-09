from django.urls import path

from .views import UserAPIView, RegisterAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    # path('login/', LoginAPIView.as_view()),
    # path('logout/', LogoutView.as_view(), name='knox_logout'),
    # path('logoutall/', LogoutAllView.as_view(), name='knox_logoutall')
]
