from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from customuser.models import Address

User = get_user_model()

class RegisterForm(forms.ModelForm):
    """
    The default
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

class Meta:
    model = User
    fields = ['email', 'phone', 'firstname', 'lastname']

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("l'e-mail est pris")
        return email

    def clean(self):
        '''
        Vérifiez que les deux mots de passe correspondent.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data


class UserAdminCreationForm(forms.ModelForm):
    """
    Un formulaire pour créer de nouveaux utilisateurs. Comprend tout le nécessaire
    champs, plus un mot de passe répété.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'firstname', 'lastname', 'phone' ]
        

    def clean(self):
        '''
        Vérifiez que les deux mots de passe correspondent.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Enregistrez le mot de passe fourni au format haché
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """Un formulaire pour mettre à jour les utilisateurs. Inclut tous les champs sur
    l'utilisateur, mais remplace le champ du mot de passe par celui de l'administrateur
    champ d'affichage du hachage du mot de passe.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active', 'admin','firstname', 'lastname', 'phone']

        def clean_password(self):
            # Indépendamment de ce que l'utilisateur fournit, renvoie la valeur initiale.
            # Cela se fait ici, plutôt que sur le terrain, car le
            # le champ n'a pas accès à la valeur initiale
            return self.initial["password"]


# class MyAddressForm(forms.ModelForm):
#     def __iter__(self):
#       for item in self.items.all():
#          yield item
#     # def __init__(self, *args, **kwargs):
#     #     super(MyAddressForm, self).__init__(*args, **kwargs)
#     #     ## add a "form-control" class to each form input
#     #     ## for enabling bootstrap
#     #     for name in self.fields.keys():
#     #         self.fields[name].widget.attrs.update({
#     #             'class': 'form-control'
#     #             # 'type': 'hidden'
#     #         })
    # class Meta:
    #     model = Address
    #     fields = "__all__"