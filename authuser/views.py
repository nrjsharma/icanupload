from django.shortcuts import render  # NOQA
from django.views import View


class SignUpView(View):

    def get(self, request):
        return render(request, 'authuser/signup.html')


class LogInView(View):

    def get(self, request):
        return render(request, 'authuser/login.html')
