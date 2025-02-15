from django.contrib import admin
from django.urls import path

from core.apps.items.views import (
    AdminItemsListView,
    ItemCreateView,
    ItemDetailedView,
    ItemUpdateView,
    UserInventory,
    UserItemsListView,
    cancel_rent,
    item_delete,
    item_rent,
)
from core.apps.organizations.views import AdminNoOrganization
from core.apps.purchases.views import PurchasesCreateView, PurchasesListView, purchase_delete
from core.apps.reports.views import BrokenReport, InUseReport, NewReport
from core.apps.requests.views import (
    AdminCreationRequestListView,
    CreationRequestCreateView,
    CreationRequestListView,
    JoinRequestAdminListView,
    JoinRequestCreateView,
    JoinRequestMonitor,
    RepairRequestAdminListView,
    RepairRequestCreateView,
    RepairRequestListView,
    creation_request_accept,
    creation_request_decline,
    join_request_accept,
    join_request_decline,
    repair_request_accept,
    repair_request_decline,
)
from core.apps.users.views import (
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
    path("items/inventory/user", UserInventory.as_view(), name="user-inventory"),
    path("items/rent/<int:pk>", item_rent, name="item-rent"),
    path("items/rent/cancel/<int:pk>", cancel_rent, name="item-rent-cancel"),
    path("items/item/detailed/<int:pk>", ItemDetailedView.as_view(), name="item-detailed"),
    path("organizations/create", AdminNoOrganization.as_view(), name="organization-create"),
    path(
        "requests/join_requests/admin",
        JoinRequestAdminListView.as_view(),
        name="requests-admin-join-view",
    ),
    path(
        "request/creation_requests/view",
        CreationRequestListView.as_view(),
        name="requests-creation-view",
    ),
    path(
        "request/creation_requests/admin/view",
        AdminCreationRequestListView.as_view(),
        name="requests-creation-view-admin",
    ),
    path(
        "request/creation_requests/create",
        CreationRequestCreateView.as_view(),
        name="requests-creation-create",
    ),
    path(
        "request/creation_requests/decline/<int:pk>",
        creation_request_decline,
        name="requests-creation-decline",
    ),
    path(
        "request/creation_requests/accept/<int:pk>",
        creation_request_accept,
        name="requests-creation-accept",
    ),
    path(
        "requests/join_requests/decline/<int:pk>",
        join_request_decline,
        name="requests-admin-join-decline",
    ),
    path(
        "requests/join_requests/accept/<int:pk>",
        join_request_accept,
        name="requests-admin-join-accept",
    ),
    path(
        "request/repair_request/add/<int:pk>",
        RepairRequestCreateView.as_view(),
        name="requests-repair-add",
    ),
    path(
        "requests/repair_requests/admin",
        RepairRequestAdminListView.as_view(),
        name="requests-admin-repair-view",
    ),
    path(
        "requests/repair_requests/decline/<int:pk>",
        repair_request_decline,
        name="requests-admin-repair-decline",
    ),
    path(
        "requests/repair_requests/accept/<int:pk>",
        repair_request_accept,
        name="requests-admin-repair-accept",
    ),
    path("requests/user", RepairRequestListView.as_view(), name="requests-user-view"),
    path("purchases/view", PurchasesListView.as_view(), name="purchase-view"),
    path("purchases/create", PurchasesCreateView.as_view(), name="purchase-create"),
    path("purchases/delete/<int:pk>", purchase_delete, name="purchase-delete"),
    path("reports/in_use", InUseReport.as_view(), name="report-in-use"),
    path("reports/broken", BrokenReport.as_view(), name="report-broken"),
    path("reports/new", NewReport.as_view(), name="report-new"),
]
