from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import Group, Permission
from django.urls import reverse 

class UserManager(BaseUserManager):
    """model gestion"""
    def create_user(self, email, password=None):
        """
        Crée et enregistre un utilisateur avec l'e-mail et le mot de passe donnés.
        """
        if not email:
            raise ValueError('Les utilisateurs doivent avoir une adresse e-mail')
        user = self.model(
                        email=self.normalize_email(email),
                        )


        user.set_password(password)
        user.save(using=self._db)
        return user




    def create_staffuser(self, email, password):
        """
        Crée et enregistre un utilisateur du staff avec l'e-mail et le mot de passe donnés.
        """
        user = self.create_user(
        email,
        password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user




    def create_superuser(self, email, password):
        """
        Crée et enregistre un superutilisateur avec l'e-mail et le mot de passe donnés.
        """
        user = self.create_user(
        email,
        password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user






class User(AbstractBaseUser):
    
    objects = UserManager()
    
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # condition
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    
    #group and permission
    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)
    
    # personnal info
    phone = models.CharField(max_length=20, blank=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    
    
    # for email is a username 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password sont requis par défaut.
    def get_full_name(self):
        # L'utilisateur est identifié par son adresse e-mail
        return self.email
    
    def get_short_name(self):
        # L'utilisateur est identifié par son adresse e-mail
        return self.email
    
    def __str__(self):
        return self.email
    

    
    def has_perm(self, perm, obj=None):
        "L'utilisateur a-t-il une autorisation spécifique ?"
        # Réponse la plus simple possible : Oui, toujours
        return True
    
    def has_module_perms(self, app_label):
        "L'utilisateur dispose-t-il des autorisations nécessaires pour voir l'application ?`app_label`?"
        # Réponse la plus simple possible : Oui, toujours
        return True
    
    @property
    def is_staff(self):
        "L'utilisateur est-il un membre du personnel ?"
        return self.staff
    
    @property
    def is_admin(self):
        "L'utilisateur est-il un membre administrateur?"
        return self.admin
    
Userr = get_user_model()
class Address(models.Model):
    user = models.ManyToManyField(Userr)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=127)
    city = models.CharField(max_length=127)
    country = models.CharField(max_length=127)
    zipcode = models.CharField(max_length=127)
    phone = models.CharField(max_length=20, blank=True)
    default = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("address_update", kwargs={"pk": self.pk})
    
    
