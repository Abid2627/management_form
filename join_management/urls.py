from django.urls import path
from .views import management_join_form
from join_management.views import display_data
from . import  views
urlpatterns = [
    path('join/', management_join_form, name='management_join_form'),
    path('success/', views.success_view, name='success'),
    path('display-data/', display_data, name='display_data'),
]

