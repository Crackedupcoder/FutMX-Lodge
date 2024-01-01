from django.shortcuts import render
from .forms import EmailContactForm
from django.core.mail import send_mail
from django.http import JsonResponse
from lodges.models import Room, Lodge
from lodges.views import price_choices
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = EmailContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['subject']} from {cd['name']} with email {cd['email']}"
            message = f"{cd['message']}"
            print(f"Subject: {subject}")
            print(f"Message: {message}")
            send_mail(subject, message, 'futmxlodge@gmail.com', ['futmxlodge@gmail.com'])
            messages.success(request, "Your Message has been Successfully Sent We Would get back to you as Soon as Possible, If you want a Quicker response Please Contact us via Phone or Any of our Social Media Pages")
        else:
            messages.error(request, "An Error Occured Please Try Again")
    else:
        form = EmailContactForm()
    return render(request, 'contact/contact.html', {'form':form,
                                    'campus_choices': Lodge.Campus.choices,
                                    'type_choices': Room.RoomType.choices,
                                    'water_choices': Lodge.Water.choices,
                                    'light_choices': Lodge.Light.choices,
                                    'price_choices': price_choices,
                                    'values':request.GET,})
