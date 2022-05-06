from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.ListAllPropertiesAPIView.as_view(), name="all-properties"),
    path("agents/", views.ListAgentsPropertiesAPIView.as_view(), name="agent-properties"),
    path("details/<slug:slug>/", views.PropertyDetailView.as_view(), name="property-detail"),
    path("search/<slug:slug>/", views.PropertySearchAPIView.as_view(), name="property-search"),
    path("create/", views.create_property_api_view, name="prpoerty-create"),
    path("update/<slug:slug>/", views.update_property_api_view, name="property-update"),
    path("delete/<slug:slug>/", views.delete_property_api_view, name="delete-property"),
]
