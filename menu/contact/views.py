from contact.models import Contact
from contact.forms import ContactForm
from django.views.generic import CreateView
from contact.service import send
#from .tasks import send_spam_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = 'contact/tags/form.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)
