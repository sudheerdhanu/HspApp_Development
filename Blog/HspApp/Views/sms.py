from django.shortcuts import render
from django.template import loader

from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse


def send(request):
    user_name="sudheer"
    html_message = loader.render_to_string(
        'security\mail_response.html',
        {
            'user_name': user_name,
            'subject': 'Thank you from' + 'dynymic_data',

    })

    subject="Hospectile Registration"
    message="Hello "+user_name+ 'You have registered sucessfully'
    from_email='smreddy475@gmail.com'
    to_list=('smreddy475@gmail.com',)


    # email = EmailMessage('resume', 'sudheer hi', to=['smreddy475@gmail.com'])
    send_mail(subject, message, from_email, to_list, fail_silently=True, html_message=html_message)
    # email.send()
    return HttpResponse("sent")

