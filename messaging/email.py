from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


class EmailCustom():
    
    @staticmethod
    def send_html_email(*args, **kwargs):
        from_email = kwargs.get('from_email', 'default@email.from')
        context = dict(kwargs.get('context'))
        template = get_template(kwargs.get('template_name'))
        body = template.render(context)
        subject = kwargs.get('subject', 'Default subject here')
        headers = kwargs.get('headers', {})

        message = EmailMultiAlternatives(
                subject,
                from_email,
                kwargs.get('to'),
                headers=headers
            )

        message.attach_alternative(body, 'text/html')
        message.send(fail_silently=False)