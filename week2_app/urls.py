from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_subscriber),
    path('char_count', views.char_count, name="char_count")
]