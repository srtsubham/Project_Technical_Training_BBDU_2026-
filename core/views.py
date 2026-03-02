from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .models import Enrollment


class LV(LoginView):
    template_name = "core/login.html"


class LOV(LogoutView):
    next_page = "login"


class RV(CreateView):
    form_class = UserCreationForm
    template_name = "core/register.html"
    success_url = reverse_lazy("login")


class DV(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c["e"] = Enrollment.objects.filter(u=self.request.user)
        return c
