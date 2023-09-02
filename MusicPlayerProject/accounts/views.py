from django.shortcuts import render, redirect
from django.views import View
from .backends import EmailOrUsernameBackend
from .forms import LoginForm, SignUpForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.


class LoginView(View):
    template_name = "registration/"
    login_form = ""

    def get(self, request, *args, **kwargs):
        logform = self.login_form
        logform.fields['username'].required = False  # Make username field optional
        logform.fields['username'].widget.attrs['placeholder'] = 'Username or Email'  # Change placeholder
        context = {"form":logform}
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = self.login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
        user = EmailOrUsernameBackend.authenticate(self, request, username=username, password=password,)
        if user:
            login(request, user, backend="accounts.backends.EmailOrUsernameBackend")
            messages.success(request, "Login Successful! Music Loading...", "success")
            return redirect("home")
        messages.error(request, "Wrong Data! Please try again!", "warning")
        return redirect("login")

        
