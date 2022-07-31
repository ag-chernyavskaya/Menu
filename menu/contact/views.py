from .models import Contact
from .forms import ContactForm
from django.views.generic import CreateView
from .service import send
from .tasks import send_info_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = 'contact/tags/form.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        #send_info_email.delay(form.instance.email)
        return super().form_valid(form)
