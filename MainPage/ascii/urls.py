
from django.urls import path
from . import views
urlpatterns = [
    path('plus',views.AsciiViewPlus.as_view()),
    path('minus',views.AsciiViewMinus.as_view()),
    path('reverse',views.AsciiViewReverse.as_view()),
]
