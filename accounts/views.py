from django.shortcuts import render
from accounts.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import login, logout, views
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignUp(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("accounts:login")
    template_name = "signup.html"


def profile_view(request):
    # u = User.objects.get(username=username)
    return render(request, 'accounts/profile_detail.html')
