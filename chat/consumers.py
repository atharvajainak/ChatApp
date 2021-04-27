from django.contrib.auth import get_user_model
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Group, Message

User = get_user_model()

class ChatConsumer(WebsocketConsumer):
    def message_to_json(self, msg):
        return {
            'author': msg.author.username,
            'content': msg.message_text,
            'timestamp': str(msg.message_datetime)
        }

    def messages_to_json(self, msgs):
        result = []
        for msg in msgs:
            result.append(self.message_to_json(msg))
        return result

    def fetch_messages(self, data):
        msgs = Group.objects.filter(group_name=self.room_name)[0].last_10_messages(1)
        content = {
           'messages': self.messages_to_json(msgs)
        }
        self.send_mesage(content)


    def new_message(self, data):
        author = data['from']
        author_user = User.objects.filter(username=author)[0]
        group_object = Group.objects.filter(group_name=self.room_name)[0]
        message = Message.objects.create(
            group = group_object,
            author=author_user,
            message_text= data['message']
        )
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)


    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_mesage(self, message):
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))


    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))