from django.urls import path

from . import views
from .views import Contact

urlpatterns = [
    path('contact', views.contact, name='contact')
    # path('contact', Contact.as_view(), name='contact')
]
