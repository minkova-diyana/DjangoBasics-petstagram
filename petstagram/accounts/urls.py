from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('profile/<int:pk>', include([
        path('', views.profile_details_page, name='profile-details'),
        path('edit/', views.profile_edit_page, name='profile-edit'),
        path('delete/', views.profile_delete_page, name='profile-delete')
    ])),
]
