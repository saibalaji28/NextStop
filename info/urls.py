from django.urls import path
from .views import faq, about

urlpatterns = [
    path("faq/", faq, name="faq"),
    path("about/", about, name="about"),
]