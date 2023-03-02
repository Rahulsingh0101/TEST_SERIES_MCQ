from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index),
    path('addquestion/', views.addquestion),
    path('questions/', views.questions),
    path('attem/', views.attem),
    path('question_detail_view/<int:id>/', views.question_detail_view),


]
