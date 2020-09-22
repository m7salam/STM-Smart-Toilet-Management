from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models
from dashboard.models import Company

class UserManager(BaseUserManager):

    def create_user(self, email, company=None, full_name=None, password=None, is_client=False,  is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password!")
        # if not full_name:
        #     raise ValueError("Users must have full name!")
        # if not company:
        #     raise ValueError ("Client Accounts must have Company name!")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
            company = company
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.client = is_client
        user_obj.save(self._db)
        return user_obj

    def create_staffuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self,email , company=None, full_name=None, password=None):
        user = self.create_user(
            email,
            company,
            full_name=full_name,
            password=password,
            is_staff=True,
            is_admin=True,
            is_client=True
        )
        return user

    def create_client(self, email, company,  full_name=None, password=None):
        user = self.create_user(
            email,
            company,
            full_name=full_name,
            password=password,
            is_staff=False,
            is_admin=False,
            is_client=True
        )
        return user

class User(AbstractBaseUser):
    email               = models.EmailField(max_length=255, unique=True)
    full_name           = models.CharField(max_length=255, blank=True, null=True)
    active              = models.BooleanField(default=True)
    staff               = models.BooleanField(default=False)
    admin               = models.BooleanField(default=False)
    client              = models.BooleanField(default=False)
    timestamp           = models.DateTimeField(auto_now_add=True)
    company             = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    #confirm             = models.BooleanField(default=False)
    #confirmed_date      = models.DateTimeField(default=False)



    USERNAME_FIELD = 'email'  #username
    #email and password are required by default
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def get_company(self):
        return self.company

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_client(self):
        return self.client


class Email(models.Model):
    email = models.EmailField(max_length=255)
    threshold = models.IntegerField()

    def __str__(self):
        return self.email



























# class Company(models.Model):
#     name = models.CharField(max_length=500)
#
#     def __str__(self):
#         return self.name
#
#
# class Client(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     organization = models.ManyToManyField(Company)
#
#     def __str__(self):
#         if self.user.username is None:
#             return "ERROR-CLIENT NAME IS NULL"
#         return self.user.username
