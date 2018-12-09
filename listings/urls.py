from django.urls import path
from listings.views import Index, DetailListing
from . import views

urlpatterns = [
    # path('', views.index, name='listings'),
    # path('<int:listing_id>', views.listing, name='listing'),\
    path('', Index.as_view(), name='listings'),
    path('<slug:slug>/', DetailListing.as_view(), name='listing'),
    path('search', views.search, name='search')
]