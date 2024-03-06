from django import forms
from .models import JoinManagement

class JoinManagementForm(forms.ModelForm):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES)

    class Meta:
        model = JoinManagement
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')
        if JoinManagement.objects.filter(email=email).exists():
            self.add_error('email', 'This email address is already registered.')
        if JoinManagement.objects.filter(phone_number=phone_number).exists():
            self.add_error('phone_number', 'This phone number is already registered.')

        return cleaned_data
