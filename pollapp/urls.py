# pollingProject/voterAPI/urls.py : App urls.py
from django.urls import path, include
from pollapp import views

#logger = logging.getLogger('root')

urlpatterns = [
    path('pollapp/', views.poll.as_view({'get': 'get', 'post': 'post'})),  
    path('pollapp/<int:id>',views.poll.as_view({'put': 'put'}) )  
    #path('pollapp/', views.userviews.as_view())
]