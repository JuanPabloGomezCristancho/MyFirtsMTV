from django.urls import path
from Family import views

app_name = "Family"
urlpatterns = [
    path("relatives", views.relatives, name="Relative-list"),
]
