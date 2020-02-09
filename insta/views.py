from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView
from django.contrib import messages
from .models import Post
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'insta/home.html',category)

class PostListView(ListView):
    model = Post
    template_name = 'insta/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    
def register(request):
    '''
    function that renders the renders the registration form
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has  been created.You are now able to login')#flash message
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'insta/profile.html')
    
    
