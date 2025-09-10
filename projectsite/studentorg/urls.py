from django.urls import path
from . import views
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Use the class-based view
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),  # Added trailing slash
    path('organization_list/<pk>',OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization- delete'),
]
