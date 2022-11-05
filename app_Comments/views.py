from rest_framework import status, generics, views
from rest_framework.permissions import AllowAny

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .models import Comments
from .serializers import ListCreateCommentSerializer


class CreateCommentView(generics.ListCreateAPIView):
    serializer_class = ListCreateCommentSerializer
    permission_classes = [AllowAny, ]
    queryset = Comments.objects.filter(accepted=True).order_by('?')[0:12]


class ListAllCommentsView(LoginRequiredMixin, ListView):
    model = Comments
    paginate_by = 15
    template_name = 'comments/comments.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListAllCommentsView, self).get_context_data(**kwargs)
        context['unconfirmed'] = Comments.objects.filter(accepted=False)
        context['confirmed'] = Comments.objects.filter(accepted=True)
        return context


class ConfirmCommentView(LoginRequiredMixin, UpdateView):
    model = Comments
    success_url = reverse_lazy("comments:listcomments")

    def get_success_url(self):
        return HttpResponseRedirect(reverse("comments:listcomments"))

    def get_queryset(self):
        return Comments.objects.filter(accepted=False)

    def get(self, request, *args, **kwargs):
        comment_object = self.get_object()
        if comment_object:
            comment_object.accepted = True
            comment_object.save()
            return self.get_success_url()


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comments
    success_url = reverse_lazy("comments:listcomments")

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
