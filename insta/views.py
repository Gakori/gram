from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView
from django.contrib import messages
from .models import Post
from .forms import UserRegisterForm
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
    return render(request, 'insta/profile.html')
    
    
