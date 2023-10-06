from django.urls import path

from . import views


urlpatterns = [
    path("data/", views.DataListView.as_view()),
    path("data/<int:pk>/", views.DataDetailView.as_view())
]