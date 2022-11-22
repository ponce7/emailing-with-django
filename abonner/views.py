from django.shortcuts import render

from django.core.mail import send_mail 
from django.conf import settings
from abonner.forms import ContactUsForm


def contact(request):
    if request.method == 'POST':
      
        form = ContactUsForm(request.POST)
        
        if form.is_valid():
                subject = 'Merci de vous être inscrit sur notre site' 
                message = ' cela signifie un monde pour nous ' 
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = ['receiver @gmail.com ']
                send_mail(subject, message, email_from, recipient_list)
        else:
            
            form = ContactUsForm()


    return render(request,'contact.html',{'form': form})
    