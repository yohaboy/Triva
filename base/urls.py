from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name='home'),
    path('rank/' ,views.rank,name='rank'),
    path('profile/' ,views.profile,name='profile'),
    path('quiz/<int:id>',views.quizPage ,name='quiz')
]
