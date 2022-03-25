from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import RedirectView

from .models import ChatGroup
from tortoise import Tortoise
from django.conf import settings
from asgiref.sync import sync_to_async
from .tortoise_models import ChatMessage


def index(request):
    # return render(request, 'chat/chat_home.html')
    all_users = User.objects.all().filter().exclude(username=request.user.username)
    all_users_with_group_id = []

    for i in all_users:
        for group in ChatGroup.objects.all():
            if i in User.objects.filter(groups__id=group.id) and request.user in User.objects.filter(
                    groups__id=group.id):
                # print("Yes")
                all_users_with_group_id.append({'username': i.username, 'group_chat_no': group.id})
    # print(all_users_with_group_id[0]['group_chat_no'])
    return redirect(RoomRedirectView.get_redirect_url(request, all_users_with_group_id[0]['group_chat_no']))


def get_participants(group_id=None, group_obj=None, user=None):
    """ function to get all participants that belong the specific group """

    if group_id:
        chatgroup = ChatGroup.objects.get(id=id)
    else:
        chatgroup = group_obj

    temp_participants = []
    for participants in chatgroup.user_set.values_list('username', flat=True):
        if participants != user:
            temp_participants.append(participants.title())
    temp_participants.append('You')
    return ', '.join(temp_participants)


class RoomRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, room_id):
        # it would be better to use reverse here
        return '/chat/%s/' % room_id


def room(request, group_id):
    if request.user.groups.filter(id=group_id).exists():
        chatgroup = ChatGroup.objects.get(id=group_id)
        # TODO: make sure user assigned to existing group
        assigned_groups = list(request.user.groups.values_list('id', flat=True))
        groups_participated = ChatGroup.objects.filter(id__in=assigned_groups)

        # print(ChatGroup.objects.get(name='arpansahutechnorigger'))
        # # print(ChatGroup)
        # print(User.objects.filter(groups__id=3))
        #
        # print(chatgroup, assigned_groups, groups_participated)
        chat_name = ''
        for participants in chatgroup.user_set.values_list('username', flat=True):
            if participants != request.user.username:
                print(participants)
                chat_name += participants

        all_users = User.objects.all().filter().exclude(username=request.user.username)
        all_users_with_group_id = []

        # print(get_participants(group_obj=chatgroup, user=request.user))
        for i in all_users:
            for group in ChatGroup.objects.all():
                if i in User.objects.filter(groups__id=group.id) and request.user in User.objects.filter(
                        groups__id=group.id):
                    # print("Yes")
                    all_users_with_group_id.append({'username': i.username, 'group_chat_no': group.id})

        # print(all_users_with_group_id)
        int_group_id = int(group_id)
        return render(request, 'chat/room.html', {
            'roomName': chatgroup,
            # 'participants': get_participants(group_obj=chatgroup, user=request.user.username),
            # 'groups_participated': groups_participated,
            'all_users': all_users_with_group_id,
            'current_user_id': request.user.id,
            'int_group_id': int_group_id,
            'chat_name': chat_name
        })
    else:
        return HttpResponseRedirect(reverse("unauthorized"))


def unauthorized(request):
    return render(request, 'chat/unauthorized.html', {})


async def history(request, room_id):
    await Tortoise.init(**settings.TORTOISE_INIT)
    chat_message = await ChatMessage.filter(room_id=room_id).order_by('date_created').values()
    await Tortoise.close_connections()

    return await sync_to_async(JsonResponse)(chat_message, safe=False)


@sync_to_async
def get_current_user(request):
    return str(request.user.username).capitalize()


async def delete_all_messages(request, id):
    username = await get_current_user(request)

    await Tortoise.init(**settings.TORTOISE_INIT)
    chat_message = await ChatMessage.filter(room_id=id, username=username).delete()
    await Tortoise.close_connections()

    return redirect(RoomRedirectView.get_redirect_url(request, id))
