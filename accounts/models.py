from django.db import models
from django.contrib.auth.models import ( 
    BaseUserManager,
    AbstractBaseUser
)
from django.core.validators import RegexValidator


USERNAME_REGEX = '^[a-zA-Z0-9_-]{3,50}$'

class UserManager(BaseUserManager):
    def create_user(self, email, username, position, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')
        if not position:
            raise ValueError('Position must be specified')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            position = position
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, position, password=None):
        user = self.create_user(
            email = email, 
            username = username,
            position = position,
            password = password
        )
        user.is_admin = True
        user.is_creater = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=50,
        unique=True,
    )
    username = models.CharField(
        max_length=50,
        validators=[
                RegexValidator(
                regex=USERNAME_REGEX,
                message='Username must be alphanumeric, may contain - or _',
                code='Invalid Username'
            )
        ],
        unique=True
    )
    POSITION = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student')
    )
    position = models.CharField(
        max_length=20,
        choices=POSITION
    )
    date_joined = models.DateField(
        verbose_name="date joined",
        auto_now_add=True
    )
    is_admin = models.BooleanField(default=False)
    is_creater = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username', 'position' ]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_info = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'