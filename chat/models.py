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