from django.db import models


from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, admission_number, university, username, phone_number, password = None, is_active = True, is_staff = False, is_admin = False):
        if not email:
            raise ValueError("User must have email address")
        if not password:
            raise ValueError("User must have password") 
        if not full_name:
            raise ValueError("User must have Fullname") 

        user_obj = self.model(
            full_name = full_name,
            admission_number = admission_number,
            university = university,
            username = username,
            phone_number = phone_number,
            email = self.normalize_email(email)

        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using = self._db)
        return user_obj
    def create_staffuser(self, email, password = None):
        user = self.create_user(
            email,
            full_name,
            admission_number,
            university,
            username,
            phone_number,
            password= password,
            is_staff = True
        )    
        return user
    def create_superuser(self, email, password = None):
        user = self.create_user(
            email,
            full_name,
            admission_number,
            university,
            username,
            phone_number,
            password= password,
            is_staff = True,
            is_admin = True
        )    
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique = True)
    # add on

    full_name = models.CharField(max_length = 254, blank=True, null=True)
    admission_number = models.CharField(max_length = 254, blank=True, null=True)
    university = models.CharField(max_length = 254, blank=True, null=True)
    username = models.CharField(max_length = 254, blank=True, null=True)
    phone_number = models.CharField(max_length = 254, blank=True, null=True)

    # end add on
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("Email Already Exists")
        return email

    def clean_admission_number(self):
        admission_number = self.cleaned_data.get('admission_number')
        qs = User.objects.filter(admission_number = admission_number)
        if qs.exists():
            raise forms.ValidationError("Admission Number Already Register If It iy You Move To Login Page")
        return admission_number

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        qs = User.objects.filter(phone_number = phone_number)
        if qs.exists():
            raise forms.ValidationError("That Number Already Register")
        return phone_number  
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'admission_number', 'university', 'username', 'phone_number', ]
    objects = UserManager()
    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email
    def has_perm(self, perm, obj = None):
        return True
    def has_module_perms(self,app_label):
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






# class MyUserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         if not email:
#             raise ValueError('Users must have email')
#         user = self.model(
#             username=username,
#             email=self.normalize_email(email)
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None):
#         if not email:
#             raise ValueError("User must have an email")
#         if not password:
#             raise ValueError("User must have a password")
#         user = self.create_user(username, email, password=password)

#         user = self.model(
#             email=self.normalize_email(email)
#         )

#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


# class MyUser(AbstractBaseUser):
#     username = models.CharField(
#         max_length=300,
#         validators=[
#             RegexValidator(regex=USERNAME_REGEX,
#                            message='username must be alphanumeric or Contain numbers',
#                            code='invalid username'
#                            )
#         ],
#         unique=True
#     )
#     # email = models.EmailField(max_length=254, unique=True, verbose_name='email address')
#     email = models.EmailField('email address', unique=True, max_length=255)
#     is_admin = models.BooleanField(default=False)

#     is_staff = models.BooleanField(('staff status'), default=False)

#     objects = MyUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
