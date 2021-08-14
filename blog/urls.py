from django.urls import path
from blog.views import contact, home


urlpatterns = [
    path('', home, name="home"),
    path('contact', contact, name="contact")
]
