# myapp/urls.py
from django.urls import path
from django.views.generic import TemplateView

from emailer.views import RegisterView, index

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/success/', TemplateView.as_view(template_name='registration/success.html'), name='register_success'),
]
