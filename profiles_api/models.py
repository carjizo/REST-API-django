from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """ Manager para Perfiles de Usuario """
    
    def create_user(self, email, name, password=None):
        """ Crear Nuevo User Profile """
        if not email:
            raise ValueError('Usuario debe tener un Email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo Base de Datos para Usuarios en el Sistema """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        ''' Obtener Nombre Completo del Usuario '''
        return self.name

    def get_short_name(self):
        ''' Obtener Nombre Corto del Usuario '''
        return self.name

    def __str__(self):
        ''' Retornar Cadena Representando Nuestro Usario '''
        return self.name

class ProfileFeedItem(models.Model):
    """ Actualiza Status Update de Perfil """
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Retorna modelo como cadena """
        return self.status_text


class Course(models.Model):
    """ Modelo Base de Datos para lso cursos en el Sistema """
    name = models.CharField(max_length=40)
    teacher = models.CharField(max_length=100)
    duration = models.PositiveSmallIntegerField(default=3)


    def __str__(self):
        ''' Retornar Cadena Representando Nuestro curso'''
        return self.name

class FatherFamily(models.Model):
    """ Modelo Base de Datos para los padres de familia en el Sistema """
    dni = models.CharField(max_length=8)
    surnames = models.CharField(max_length=40)
    names = models.CharField(max_length=40)
    birth_date = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]  
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
        txt = "{0}, {1}"
        return txt.format(self.surnames , self.names)


class Registration(models.Model):
    """ Modelo Base de Datos para las matriculas en el Sistema """
    student = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    fatherfamily = models.ForeignKey(
        FatherFamily,
        on_delete=models.CASCADE
    )
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculado en el curso {1} / Fecha: {2}"
        fecMat = self.registration_date.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.student, self.course, fecMat)

  