from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def groups(request):
    user_groups = request.user.all_groups.all()
    context = {
        'groups': user_groups,
    }
    return render(request, 'chat/groups.html', context = context)

@login_required
def selected_group(request, grp_name):
    return render(request, 'chat/group.html', {
        'grp_name': grp_name
    })

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })