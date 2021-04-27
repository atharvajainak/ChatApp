from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

GROUPNAME_REGEX = '^[a-zA-Z0-9_-]{3,50}$'
class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        validators=[
                RegexValidator(
                regex=GROUPNAME_REGEX,
                message='Group name must be alphanumeric, may contain - or _',
                code='Invalid Group name'
            )
        ],
        unique=True
    )
    group_creator = models.ForeignKey(User, related_name='groups_created', on_delete=models.CASCADE)
    group_info = models.CharField(max_length=300, blank=True, null=True)
    group_members = models.ManyToManyField(User, related_name='all_groups')

    def __str__(self):
        return self.group_name

    def last_10_messages(self, n_times):
        if n_times < 1:
            raise ValueError('Passed argument should be > 1')
        no_messages = 10 * n_times
        return self.messages.order_by('-message_datetime').all()[:10]


def get_del_user():
    return User.objects.get_or_create(username='deleted')[0]

class Message(models.Model):
    group = models.ForeignKey(Group, related_name='messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET(get_del_user))
    message_text = models.TextField()
    message_datetime = models.DateTimeField(verbose_name="date posted", auto_now_add=True)
    is_notice = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.group}: {self.message_text}'