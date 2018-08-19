from django.conf.urls import url
from pastebin import views
app_name = "pastebin"

urlpatterns = [
   
    url(r'^main_page/', views.main_page, name='main_page'),
   
   
   
]
