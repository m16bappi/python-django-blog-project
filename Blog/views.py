from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Blog


class HomeView(TemplateView):
    template_name = 'Blog/Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['data'] = Blog.objects.all()
        return context
