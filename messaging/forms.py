from dataclasses import fields
from django import forms

from messaging.models import Contact

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():

            # self.fields[name].label = ''

                
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
                'placeholder':f'Your {name}'
                #'type': 'hidden'
            })
    
    class Meta:
        model = Contact
        fields = ['subject','name', 'email', 'title', 'message', 'img']