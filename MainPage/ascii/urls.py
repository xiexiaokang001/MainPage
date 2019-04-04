
from django.urls import path
from . import views
urlpatterns = [
    path('',views.ascii),
    path('asciisubmit', views.asciisubmit)
]
