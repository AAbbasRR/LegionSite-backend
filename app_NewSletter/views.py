from rest_framework import status, generics, views
from rest_framework.permissions import AllowAny

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .serializers import CreateNewsletterSerializer
from .models import Newsletter


class CreateNewsletterView(generics.CreateAPIView):
    serializer_class = CreateNewsletterSerializer
    permission_classes = [AllowAny, ]


class ListNewsletterView(LoginRequiredMixin, ListView):
    model = Newsletter
    template_name = 'newsletter/newsletter_list.html'
    paginate_by = 15