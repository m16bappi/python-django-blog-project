from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout

from .forms import registerForm, loginForm


class registerView(FormView):
    form_class = registerForm
    template_name = 'user/Register.html'

    def form_valid(self, form):
        user = form.save()
        login(request=self.request, user=user)
        return redirect('/')


class loginView(FormView):
    form_class = loginForm
    template_name = 'user/Login.html'

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if user is not None:
            login(request=self.request, user=user)
            return redirect('/')
        else:
            return redirect('login')


def logoutView(request):
    logout(request)
    return redirect('/')
