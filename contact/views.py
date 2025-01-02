from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def home_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"Message from {name}",
                message=message,
                from_email=email,
                recipient_list=['sidickabdoulayesino1@gmail.com'],  # Replace with your email
            )
            return render(request, 'contact/success.html')  # Success page
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {'form': form})

def sidick_view(request):
    return render(request, 'contact/sidick.html')

def register_view(request):
    return render(request, 'contact/register.html')

def education_view(request):
    return render(request, 'contact/education.html')

def index1_view(request):
    return render(request, 'contact/index1.html')

def Qst3_view(request):
    return render(request, 'contact/Qst3.html')