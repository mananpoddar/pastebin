from django.conf.urls import url
from pastebin import views
app_name = "pastebin"

urlpatterns = [
   
    url(r'^main_page/', views.main_page, name='main_page'),
    url(r'^(?P<url_no>[0-9]+)/$', views.content_fetch, name='content'),
    url(r'^logged_in/(?P<url_no>[0-9]+)/$', views.content_fetch_logged_in, name='content_logged_in'),

    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^user_signup/', views.user_signup, name='user_signup'),
    url(r'^main_loggedin_page/', views.main_loggedin_page, name='main_loggedin_page'),
    url(r'^user_logout/', views.user_logout, name='user_logout'),
    url(r'^(?P<pk>[0-9]+)/update/', views.pasteupdate.as_view(), name='paste_update'),






   
   
   
]
