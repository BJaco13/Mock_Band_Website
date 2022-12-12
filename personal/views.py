from .models import Shows
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView


# Creates the ShowsListView from the model Shows and gets data to display on Shows page
class ShowsListView(ListView):
    model = Shows

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['shows_list'] = Shows.objects.all()
         return context


# Directs to the homepage / index page
def index(request):
    return render(request, "index.html")


# Directs to the products page
def products(request):
    return render (request, "products.html")


# Directs to the about page
def about_me(request):
    return render (request, "about_me.html")


# Takes the user to the shows page and sends shows data from model with for diplaying
def shows(request):
    shows = Shows.objects.all()
    shows_list = {'shows' : shows}
    return render (request, "shows1.html", shows_list)


# Authenticates the user's details then get's the 'next' query data if applicable and takes user to appropriate page
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(reverse('authentication/login'))
    else:
        login(request, user)
        next_url = request.GET.get('next')

        if next_url and len(next_url) > 0:
            return HttpResponseRedirect(next_url)
            
        else:
            return redirect('profile')


# Directs the user to the login page
def user_login(request):
    return render(request, 'authentication/login.html')


# This is used to validate the method then save the user in the model and redirect to the login page
def register_user(request):

    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))

    context = {'form': form}

    return render(request, 'authentication/register.html', context)


# Used to log the current user out
def logout_view(request):

    if request.method == 'POST':

        logout(request)
        # Redirect to a success page.
        return redirect(reverse("profile"))

# Redirects to the profile page
def profile(request):
    return render(request, 'authentication/profile.html')