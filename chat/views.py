from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Group
from django.contrib.auth import get_user_model
from .forms import GroupCreationForm

User = get_user_model()


@login_required
def groups(request):
    user_groups = sorted(request.user.all_groups.all(),key=lambda x: x.group_name)
    created_groups = sorted(request.user.groups_created.all(),key=lambda x: x.group_name)
    is_creator = str(request.user.is_creator).lower()

    form = GroupCreationForm(request.POST or None)
    if form.is_valid() and is_creator:
        group = form.save(commit=False)
        group.group_creator = request.user
        group.save()
        group.group_members.add(request.user)
        return redirect('/groups')

    context = {
        'groups': user_groups,
        'created_groups': created_groups,
        'is_creator': is_creator,
        'form' : form
    }
    return render(request, 'chat/groups.html', context = context)

@login_required
def selected_group(request, grp_name):
    try:
        group = request.user.all_groups.get(group_name=grp_name)
    except Group.DoesNotExist:
        raise Http404("Group Does not exist or You are not a member of this group")

    creator = group.group_creator
    members_list = list(sorted(group.group_members.all(),key=lambda x: x.username))
    members_list.remove(creator)

    context = {
        'group' : group,
        'creator': creator,
        'members_list' : members_list
    }
    return render(request, 'chat/group.html', context=context)

def add_users(group, user_ids):
    for user_id in user_ids:
        _user = User.objects.get(id=user_id)
        group.group_members.add(_user)

def remove_users(group, user_ids):
    for user_id in user_ids:
        _user = User.objects.get(id=user_id)
        group.group_members.remove(_user)

@login_required
def group_members(request, grp_name):
    try:
        group = request.user.groups_created.get(group_name=grp_name)
    except Group.DoesNotExist:
        raise Http404("Group Does not exist or You are not a creator of this group")

    if request.method == 'POST':
        querydict = dict(request.POST)
        if querydict.get('flag')[0] == '1':     # add users
            add_users_list = querydict.get('add_users')
            if add_users_list:
                add_users(group, add_users_list)
        elif querydict.get('flag')[0] == '-1': #remove users
            remove_users_list = querydict.get('remove_users')
            if remove_users_list:
                remove_users(group, remove_users_list)

    members_list = list(sorted(group.group_members.all(),key=lambda x: x.username))
    members_id = list(map(lambda x: x.id , members_list))
    users_list = list(sorted(User.objects.all(),key=lambda x: x.username))

    def not_member(user):
        if user in members_list:
            return False
        return True
    users_list = list(filter(not_member, users_list))
    members_list.remove(request.user)
    context = {
        'members_list': members_list,
        'users_list': users_list
    }
    return render(request, 'chat/members.html', context=context)

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })