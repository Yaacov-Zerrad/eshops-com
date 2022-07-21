from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site


from eshops import settings
from messaging.forms import ContactForm
from .email import EmailCustom
from django.template.loader import get_template

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            val = form.save()
            name = val.name
            subject_contact = val.subject
            email_to = val.email
            current_site = get_current_site(request)
            
            data_html = {'name': name, 'subject':subject_contact, 'domain':current_site.domain}
            
            # data for send email
            subject, from_email, to = 'contact es-shops', 'z0583214808@gmail.com', email_to
            text_content = 'This is an important message.'
            html_content = render_to_string('email_view/contact_response_auto.html', data_html)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect('messaging:contact_success')
    return render(request, 'messaging/contact_form.html', {'form':form})


def contact_response_auto(request):
    # data for content email
    name = 'yaacov'
    domain = 'domain'
    subject_contact = 'commande'
    current_site = get_current_site(request)
    
    data_html = {'name': name, 'subject':subject_contact, 'domain':current_site.domain}
    
    # data for send email
    subject, from_email, to = 'contact es-shops', 'z0583214808@gmail.com', 'z0583214808@gmail.com'
    text_content = 'This is an important message.'
    html_content = render_to_string('email_view/contact_response_auto.html', data_html)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return redirect('shop:index')



# def contact_response_auto(request):
#     subject = 'subject'
#     from_email = 'z0583214808@gmail.com'
#     to_email = 'z0583214808@gmail.com'
#     html_content = 'email_view/contact_response_auto.html'
#     data_email = {
#           'from_email': from_email,
#           'subject': subject,
#           'to': [to_email, ],
#           'template_name': html_content,
#           'context': {'name': 'Name of user', 'money': 1000},
#         }
#     EmailCustom.send_html_email(**data_email)
#     return redirect('shop:index')


def contact_success(request):
    return render(request, 'messaging/contact_success.html')







