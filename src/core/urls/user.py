from django.urls import path

from core.views.post import UserPostsView
from core.views.user import UserCreateView, UserListView, UserView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('<id>/', UserView.as_view(), name='user-detail'),
    path('<id>/posts', UserPostsView.as_view(), name='user-detail'),
    path('', UserListView.as_view(), name='user-list'),
]
