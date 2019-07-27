from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError


class IcanuploadUserManager(BaseUserManager):
    """
    custom user manager for Icanupload user
    this user manager is responsible for all
    CRUD operation over custom user models
    """

    def create_user(self, username=None, email=None, password=None):
        if not username or username is None:
            raise ValidationError("User must have username")
        if not email or email is None:
            raise ValidationError("User must have email address")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username,
                                email=email,
                                password=password)
        user.is_admin = True
        # user.is_staff = True
        user.save(using=self._db)
        return user


class IcanuploadUser(AbstractBaseUser):
    """
    parent class for all users in icanuplaod application
    """
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    # Personal Information
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_image = models.FileField(upload_to='authuser/profile', null=True, blank=True)  # NOQA
    # Permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    # Verification
    is_email_varified = models.BooleanField(default=False)
    # Other
    created = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created.  # NOQA
    updated = models.DateTimeField(auto_now=True)  # Automatically set the field to now every time the object is saved.  # NOQA
    objects = IcanuploadUserManager()
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    # def __str__(self):
    #     return self.get_full_name

    def get_short_name(self):
        if self.first_name:
            return self.first_name
        else:
            return self.email

    def get_full_name(self):
        if self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def display_name(self):
        if self.first_name:
            return self.first_name
        else:
            return self.email
