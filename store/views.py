from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def index(request):
    categorys = Category.objects.all()
    return render(request,'index.html', {'categorys':categorys})

def blog(request):
    blogs = Blog.objects.all()
    return render(request,'blog.html', {'blogs':blogs})

def blogentry(request, id):
    blogs = Blog.objects.all()
    blogs = Blog.objects.filter(id=id)
    return render(request,'blogentry.html', {'blogs':blogs})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            phone_no = form.cleaned_data['phone_no']
            message = form.cleaned_data['message']
            send_mail(
                subject=f'{subject}',
                message=f'Name: {name}\nEmail: {email}\nPhone Number: {phone_no}\nMessage: {message}',
                from_email=email,
                recipient_list=['christelpeeris@example.com'],  # Your email address to receive the notification
            )
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def gallery(request):
    gallerys = Gallery.objects.all()
    return render(request,'gallery.html', {'gallerys': gallerys})