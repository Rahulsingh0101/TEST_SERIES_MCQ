from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('index/', views.index),
    path('registration/', views.registration),
    path('userregistration/', views.userregistration),
    path('login/', views.login),
    path('userlogin/', views.userlogin),
    path('', views.dashboard),
    path('paper/', views.paper),
    path('addquestion/', views.addquestion),
    path('questions/', views.questions),
    path('attem/', views.attem),
    path('question_detail_view/<int:id>/', views.question_detail_view),


]
