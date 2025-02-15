from django import forms
from django.contrib.auth.models import User
from .models import Booking, Services, PricingPlan

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'service',
            'price',
            'address',
            'city',
            'province',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'service': forms.Select(attrs={'onchange': 'updatePrice()'}),  # Calls JS function to update price
            'price': forms.Select(),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'province': forms.TextInput(attrs={'placeholder': 'Province'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Services.objects.all()
        self.fields['price'].queryset = PricingPlan.objects.all()  # Initially empty
        
        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                self.fields['price'].queryset = PricingPlan.objects.filter(service_id=service_id)
            except (ValueError, TypeError):
                pass  # Invalid input; empty price queryset
        elif self.instance.pk:
            self.fields['price'].queryset = self.instance.PricingPlan_set.all()
