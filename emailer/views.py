from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from emailer.forms import EmailerUserCreationForm
from emailer.utils import send_ses_email


def index(request):
    return HttpResponse('Hello, World!')


class RegisterView(CreateView):
    model = User
    form_class = EmailerUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('register_success')

    def form_valid(self, form):
        response = super().form_valid(form)
        recipient = form.cleaned_data.get('email')
        subject = 'Registration Successful'
        body_text = 'Thank you for registering.'
        send_ses_email(recipient, subject, body_text, body_text)
        return response
