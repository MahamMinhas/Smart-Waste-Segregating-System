from django.db import models

# Create your models here.

class Settings(models.Model):
    site_title = models.CharField(max_length=100)
    system_name = models.CharField(max_length=100)
    pre_loader_video = models.FileField(upload_to='', blank=True, null=True)
    site_logo = models.ImageField(upload_to="", blank=True, null=True)
    favicon = models.FileField(upload_to="", blank=True, null=True)
    home_slider1 = models.ImageField(upload_to="", blank=True, null=True) 
    home_slider2 = models.ImageField(upload_to="", blank=True, null=True)
    home_slider3 = models.ImageField(upload_to="", blank=True, null=True)
    slider_heading1 = models.CharField(max_length=255)
    slider_heading2 = models.CharField(max_length=255)
    slider_heading3 = models.CharField(max_length=255)
    slider1_text = models.CharField(max_length=255)
    slider2_text = models.CharField(max_length=255)
    slider3_text = models.CharField(max_length=255)
    about_hero = models.ImageField(upload_to="")
    services_hero = models.ImageField(upload_to="")
    pricing_hero = models.ImageField(upload_to="")
    contact_hero = models.ImageField(upload_to="")
    faq_hero = models.ImageField(upload_to="")
    preloader_video = models.FileField(upload_to="")
    footer_desc = models.TextField()
    location=models.CharField(max_length=255)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=255)
    facebook = models.CharField(max_length=255)
    pinterest = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)

class PageType(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Unique for clear mapping
    site_title = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class About(models.Model):
    about_title = models.CharField(max_length=255)
    about_heading = models.CharField(max_length=255)
    about_text = models.TextField()
    about_img = models.ImageField(upload_to="")

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    date_published = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="")
    source_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

class WhyJoinUs(models.Model):
    title = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")
    text_1 = models.CharField(max_length=255)
    text_2 = models.CharField(max_length=255)
    number_1 = models.CharField(max_length=255)
    number_2 = models.CharField(max_length=255)


    class Meta:
        verbose_name_plural = "Why Join Us"

class WhyJoinUsSubSection(models.Model):
    why_join_us = models.ForeignKey(WhyJoinUs, on_delete=models.CASCADE, related_name='sub_sections')
    sub_heading = models.CharField(max_length=255)
    description = models.TextField()

class Services(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")


    def __str__(self):
        return self.title


class FAQ(models.Model):
    faq_question = models.CharField(max_length=255)
    faq_answer = models.TextField()

class PricingPlan(models.Model): 
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='pricing_plans')
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.CharField(max_length=50, default='per month')
    description = models.TextField(blank=True, null=True)
    features = models.TextField(help_text="Separate features with a comma.")
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.service.title} - {self.price}"

    def get_features(self):
        return self.features.split(",")
    
class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    price = models.ForeignKey(PricingPlan, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.service.title} ({self.price if self.price else 'No Plan'})"



