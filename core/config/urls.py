from django.contrib import admin
from django.urls import path

from core.apps.users.views import (
    AdminDashboard,
    UserDashboard,
    UserLoginView,
    logout_user,
    main_page,
    UserProfile,
    UserProfileUpdate,
    UserRegistration,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("", main_page, name="main-page"),
    path("dashboard/admin", AdminDashboard.as_view(), name="admin-dashboard"),
    path("dashboard/user", UserDashboard.as_view(), name="user-dashboard"),
    path("register/", UserRegistration.as_view(), name="register"),
    path("user_profile/", UserProfile.as_view(), name="user_profile"),
    path("user_profile/update_profile", UserProfileUpdate.as_view(), name="update_profile"),
]