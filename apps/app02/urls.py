from django.urls import path

from app02 import views

urlpatterns = [
    path('headinfo/', views.head_info.as_view()),
    # path('imageinfo')
]