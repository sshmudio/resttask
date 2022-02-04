from django.urls import path
from apiusers.views import UserApiView, UsersList, UserDetail

urlpatterns = [
    path('user-list/', UserApiView.as_view(), name='user-list'),  # get all user list
    path('user/', UserDetail.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),  # get user f pk
]
