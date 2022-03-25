from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('history/<str:room_id>/', views.history, name='history'),
    path('<str:group_id>/', views.room, name='room'),
    path('delete/<int:id>/', views.delete_all_messages, name="delete_all_messages"),
    path('<int:id>/', views.RoomRedirectView.as_view(), name="room_redirects"),

]
