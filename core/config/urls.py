from django.contrib import admin
from django.urls import path

from core.apps.items.views import (
    AdminItemsListView,
    ItemCreateView,
    ItemUpdateView,
    UserItemsListView,
    item_delete,
)
from core.apps.requests.views import JoinRequestCreateView, JoinRequestMonitor
from core.apps.users.views import (
    AdminDashboard,
    UserDashboard,
    UserLoginView,
    UserProfile,
    UserProfileUpdate,
    UserRegistration,
    logout_user,
    main_page,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("", main_page, name="main-page"),
    path("dashboard/admin", AdminItemsListView.as_view(), name="admin-dashboard"),
    path("dashboard/user", UserItemsListView.as_view(), name="user-dashboard"),
    path("register/", UserRegistration.as_view(), name="register"),
    path("user_profile/", UserProfile.as_view(), name="user-profile"),
    path("user_profile/update_profile", UserProfileUpdate.as_view(), name="update_profile"),
    path("join_request/create", JoinRequestCreateView.as_view(), name="join-request"),
    path("join_request/monitor", JoinRequestMonitor.as_view(), name="join-request-monitor"),
    path("items/create", ItemCreateView.as_view(), name="item-create"),
    path("items/update/<int:pk>", ItemUpdateView.as_view(), name="item-update"),
    path("items/delete/<int:pk>", item_delete, name="item-delete"),
]
