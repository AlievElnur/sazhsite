from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *
 
urlpatterns = [
    path('',RasteniyaHome.as_view(), name='home'),
    path('left/<slug:lef_slug>/', RasteniyaLeft.as_view(), name='left'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('kontakti/', kontakti, name='kontakti'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('o_nas/', o_nas, name='o_nas')
]