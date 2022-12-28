from django.shortcuts import redirect, render
from api.models import *
from .forms import *
from django.views.generic import CreateView, FormView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# Create your views here.

class UserReigtrationView(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('sign-up')

    def form_invalid(self, form):
        if form.is_valid():
            messages.success(self.request, 'Account has been created')
        else:
            messages.error(self.request, 'An error occured try again')
        return super().form_invalid(form)


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Your credentials not matching, try again")
                return render(request, "login.html", {'form':form})

class IndexView(CreateView, ListView):
    template_name = "index.html"
    form_class = PostForm
    success_url = reverse_lazy("home")
    queryset = Posts.objects.all()
    context_object_name = 'posts'

    def form_valid(self, form):
        if form.is_valid():
            form.instance.user=self.request.user
            messages.success(self.request, "New post has been uploaded")
            return super().form_valid(form)
        else:
            messages.error(self.request, "uploading failed")
            return render(self.request, "index.html", {"form":form})

    # def post(self, request, *args, **kwargs):
    #     form = PostForm(request.POST)
    #     print(request.user)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         messages.success(request, "New post has been uploaded")
    #         return redirect("home")
    #     else:
    #         messages.error(request, "uploading failed")
    #         return render(request, "index.html", {"form":form})
    