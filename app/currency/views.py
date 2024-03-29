import re
from datetime import datetime, timedelta
from currency.forms import RateForm
from currency.models import Rate, ContactUs
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from django_filters.views import FilterView
from currency.tasks import send_email_in_background
from currency.filters import RateFilter


class RateListView(FilterView):
    queryset = Rate.objects.all().select_related('source').order_by('-created')
    template_name = 'rate_list.html'
    paginate_by = 21
    filterset_class = RateFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        query_parameters = self.request.GET.urlencode()
        context['filter_params'] = re.sub(r'page=\d+', '', query_parameters).lstrip('&')

        return context


class RateDetailView(LoginRequiredMixin, DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_detail.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(DeleteView):
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')
    model = Rate

    def test_func(self):
        return self.request.user.is_superuser


class RateUpdateView(UpdateView):
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')
    model = Rate


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    fields = (
        'name',
        'email',
        'subject',
        'body'
    )

    def _send_email(self):
        # from django.conf import settings
        # recipient = settings.DEFAULT_FROM_EMAIL
        subject = 'User Contact Us'
        body = f'''
                Name: {self.object.name}
                Email: {self.object.email}
                Subject: {self.object.subject}
                Body: {self.object.body}
                '''
        eta = datetime.now() + timedelta(seconds=15)
        #   print(eta)
        send_email_in_background.apply_async(
            kwargs={
                'subject': subject,
                'body': body
            },
            eta=eta
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect
