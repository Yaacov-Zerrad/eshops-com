from django.shortcuts import redirect, render
from customuser.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# for email
from eshops import settings
from django.core.mail import send_mail, EmailMessage

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .token import generateToken


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        passwordconfirm = request.POST['password2']
        # verification
        if User.objects.filter(email=email):
            messages.error(request, 'this email already exists')
            redirect('log:register')
        if len(password)<5:
            messages.error(request, 'Please the username must be at leat 5 characters.')
            return redirect('log:register')
        if passwordconfirm != password:
            messages.error(request, 'the 2 passwords do not match')
            redirect('log:register')
        
        my_user = User.objects.create_user(email, password)
        my_user.first_name =firstname
        my_user.last_name = lastname
        my_user.phone = phone
        my_user.is_active = False
        my_user.save()
        messages.success(request, 'your account has been successfully created')
        # welcome email
        subject = "welcome to my system login site"
        message = f"welcome   {my_user.first_name}  {my_user.last_name} \n\n\n\nwe are happy to have you among us \n\n\n\n thank"
        from_email = settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        # confirm email
        current_site = get_current_site(request)
        email_subject = 'confirmation of the email address on site confirmation'
        message_confirm = render_to_string('emailconfirm.html', {
            'name': my_user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': generateToken.make_token(my_user)
        })
        email = EmailMessage(email_subject, 
                            message_confirm, 
                            settings.EMAIL_HOST_USER, 
                            [my_user.email])
        email.fail_silenty = False
        email.send()
        return redirect('log:login')
        
        
    return render(request, 'register.html')



def login_user(request):
    firstname = ''
    if request.method== 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email , password=password)
        my_user = User.objects.get(email=email)
        
        if user is not None:
            login(request, user)
            # firstname = user.first_name
            messages.success(request, 'you are connecter')
            return render(request, 'login.html' , {'firstname':firstname})
        elif my_user.is_active == False:
            messages.error(request, 'you have not confirm your account, check in your mailbox and confirm before trying again')
        else:
            messages.error(request, 'bad authentication')
            return redirect('login')
    return render(request, 'login.html' )


def logout_user(request):
    logout(request)
    messages.success(request, 'you are logout')
    return redirect('log:login')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None
        
    if my_user is not None and generateToken.check_token(my_user, token):
        my_user.is_active = True
        my_user.save()
        messages.success(request, 'your account has been activated, log in now')
        return redirect('log:login')
    else:
        messages.error(request, 'your activation failed')
        return redirect('shop:index')
    
        
        
        
        
        