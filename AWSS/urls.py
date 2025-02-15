from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home',  kwargs={'page_type_slug': 'GreenSort-home'}),
    path('about/', views.about, name='about', kwargs={'page_type_slug': 'GreenSort-About'}),
    path('services/', views.services, name='services', kwargs={'page_type_slug': 'GreenSort-Services'}),
    path('contact/', views.contact, name= 'contact', kwargs={'page_type_slug': 'GreenSort-Contact'}),
    path('blog/', views.blog, name='blog', kwargs={'page_type_slug': 'GreenSort-Blogs'}),
    path('bookings/', views.booking, name='bookings'),
    path('pricing/', views.pricing, name='pricing', kwargs={'page_type_slug': 'GreenSort-Pricing'}),
    path('faq/', views.faq,name='faq', kwargs={'page_type_slug': 'GreenSort-FAQs'}),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)