from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from .models import PageType
from django.conf import settings
from .forms import RegistrationForm, BookingForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import Http404



# Create your views here.    
def home(request, page_type_slug=None):
    if page_type_slug:
        page_type = PageType.objects.get(name=page_type_slug)
    else:
        page_type = PageType.objects.get(name='default_page')
    context ={
        'settings' : models.Settings.objects.first(),
        'page_type': page_type,
        'about': models.About.objects.first(),
        'services':models.Services.objects.all(),
        'whyjoin': models.WhyJoinUs.objects.first(),
        'whyjoin_subsec': models.WhyJoinUsSubSection.objects.all(),
        'faq':models.FAQ.objects.all(),
        'MEDIA_URL': settings.MEDIA_URL
    }
    return render(request, 'AWSS/index.html', context)

def about(request, page_type_slug=None):
    if page_type_slug:
        page_type = PageType.objects.get(name=page_type_slug)
    else:
        page_type = PageType.objects.get_or_create(name='default_page')
    context ={
        'settings' : models.Settings.objects.first(),
        'page_type': page_type,
        'about': models.About.objects.first(),
        'whyjoin': models.WhyJoinUs.objects.first(),
        'whyjoin_subsec': models.WhyJoinUsSubSection.objects.all(),
        'MEDIA_URL': settings.MEDIA_URL
     }
    return render(request, 'AWSS/about.html', context)
def blog(request, page_type_slug=None):
    try:
        if page_type_slug:
            page_type = PageType.objects.get(name=page_type_slug)
        else:
            page_type = PageType.objects.get(name='blog')
    except PageType.DoesNotExist:
        # If the PageType does not exist, you can raise an error or create a fallback
        raise Http404("PageType does not exist")  # Or set a default page_type
    
    context = {
        'settings': models.Settings.objects.first(),  # Retrieve the first settings object
        'page_type': page_type,  # Retrieved or fallback page_type
        'blogs': models.Blog.objects.all().order_by('-date_published'),  # Latest blogs first
        'MEDIA_URL': settings.MEDIA_URL  # Ensure that MEDIA_URL is passed to the template
    }
    
    return render(request, 'AWSS/blog.html', context)

def services(request, page_type_slug=None):
    if page_type_slug:
        page_type = PageType.objects.get(name=page_type_slug)
    else:
        page_type = PageType.objects.get(name='default_page')
    context ={
        'settings' : models.Settings.objects.first(),
        'page_type': page_type,
        'services':models.Services.objects.all(),
        'MEDIA_URL': settings.MEDIA_URL
     }
    return render(request, 'AWSS/what-do.html', context)

def contact(request, page_type_slug=None):
    if page_type_slug:
        page_type = PageType.objects.get(name=page_type_slug)
    else:
        page_type = PageType.objects.get(name='default_page')
    context ={
        'settings' : models.Settings.objects.first(),
        'page_type': page_type,
        'MEDIA_URL': settings.MEDIA_URL
     }
    return render(request, 'AWSS/contact.html', context)

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Service Booked Successfully!")
            return redirect('services') 
    else:
        form = BookingForm()
    context = {
        'settings': models.Settings.objects.first(),  # Retrieve the first settings object
        'MEDIA_URL': settings.MEDIA_URL,  # Ensure that MEDIA_URL is passed to the template
        'form':form
    }
    return render(request, 'AWSS/booking.html', context)

def faq(request, page_type_slug=None):
    if page_type_slug:
        page_type = PageType.objects.get(name=page_type_slug)
    else:
        page_type = PageType.objects.get(name='default_page')
    context ={
        'settings' : models.Settings.objects.first(),
        'page_type': page_type,
        'faq':models.FAQ.objects.all(),
        'MEDIA_URL': settings.MEDIA_URL
     }
    return render(request, 'AWSS/FAQ.html', context)

def pricing(request, page_type_slug=None):
    if page_type_slug:
        page_type = PageType.objects.get(name=page_type_slug)
    else:
        page_type = PageType.objects.get(name='default_page')
    context ={
        'settings' : models.Settings.objects.first(),
        'page_type': page_type,
        'MEDIA_URL': settings.MEDIA_URL
     }
    return render(request, 'AWSS/pricing.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Add success message
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('login')  # Redirect to login page
        else:
            # Add error message for invalid form
            messages.error(request, "There was an error in your form. Please correct it and try again.")
    else:
        form = RegistrationForm()
    return render(request, 'AWSS/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Your account has been successfully logged in.")
            return redirect('home')  # Replace 'home' with your home page URL name
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    return render(request, 'AWSS/login.html') 

def logout_view(request):
    logout(request)
    return redirect('login')