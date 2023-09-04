from django.shortcuts import render, redirect
from django.views import View
from .backends import EmailOrUsernameBackend
from .forms import LoginForm, SignUpForm
from django.contrib.auth import login, logout
from django.contrib import messages
# Create your views here.


class LoginView(View):
    template_name = "registration/login.html"
    login_form = LoginForm

    def get(self, request, *args, **kwargs):
        logform = self.login_form
        logform.fields['username'].required = False  # Makes username field optional
        logform.fields['username'].widget.attrs['placeholder'] = 'Username or Email'  # Changes placeholder
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
        messages.error(request, "Wrong Login Data! Please try again!", "warning")
        return redirect("login")



class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("home")
    


class SignUpView(View):
    template_view = "registration/signup.html"
    signup_form = SignUpForm

    def get(self, request, *args, **kwargs):
        signform = self.signup_form
        context = {"form":signform}
        return render(request, self.template_view, context)


    def post(self, request, *args, **kwargs):
        form = self.signup_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = user.password
            user.set_password(password)
            form.save()
            return redirect("home")
        else:
            messages.error(request, "Entered data could not be Validated! Please try again.", "warning")
            return redirect("signup")