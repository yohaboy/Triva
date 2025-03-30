from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home ,name='home'),
    path('rank/' ,views.rank,name='rank'),
    path('profile/' ,views.profile,name='profile'),
    path('quiz/<int:id>',views.quizPage ,name='quiz'),
    path('quizApi/<int:id>',views.quizApi ,name='quizApi'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)