from django.urls import path
from . import views


app_name = 'a_users'

urlpatterns = [
    path('profile/', view=views.profile_view, name='profile'),
    path('profile/edit/', view=views.profile_edit_view, name='profile-edit')
]