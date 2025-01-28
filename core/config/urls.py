from django.contrib import admin
from django.urls import path

from core.apps.items.views import (
    AdminItemsListView,
    ItemCreateView,
    ItemUpdateView,
    UserItemsListView,
    UserInventory,
    ItemDetailedView,
    item_delete,
    item_rent,
    cancel_rent,
)
from core.apps.requests.views import JoinRequestCreateView, JoinRequestMonitor, JoinRequestAdminListView,RepairRequestCreateView, join_request_decline, join_request_accept
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
from core.apps.organizations.views import AdminNoOrganization


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
    path("items/inventory/user", UserInventory.as_view(), name='user-inventory'),
    path("items/rent/<int:pk>", item_rent, name="item-rent"),
    path("items/rent/cancel/<int:pk>", cancel_rent, name="item-rent-cancel"),
    path("items/item/detailed/<int:pk>", ItemDetailedView.as_view(), name="item-detailed"),
    path('organizations/create', AdminNoOrganization.as_view(), name="organization-create"),
    path('requests/join_requests/admin', JoinRequestAdminListView.as_view(), name='requests-admin-join-view'),
    path('requests/join_requests/decline/<int:pk>', join_request_decline, name='requests-admin-join-decline'),
    path('requests/join_requests/accept/<int:pk>', join_request_accept, name='requests-admin-join-accept'),
    path('request/repair_request/add', RepairRequestCreateView.as_view(), name='requests-repair-add')
]
