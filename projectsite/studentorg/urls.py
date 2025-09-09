from django.urls import path
from . import views
from studentorg.views import HomePageView, OrganizationList

urlpatterns = [
    path('', views.home, name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
]
