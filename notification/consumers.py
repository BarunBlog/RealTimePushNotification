import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"

        # Adding room_name and group_name to the channel
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept() # accept the request from frontend
        self.send(text_data=json.dumps({'status': "connected from django channels"})) # send data to frontend

    def receive(self, text_data):
        # receive data given from frontend
        print(text_data)
        self.send(text_data=json.dumps({"status": "Data received"}))

    def disconnect(self, *args, **kwargs):
        print('disconnected')


    # custom function
    def send_notification(self, event):
        data = json.loads(event.get('value')) # converting to json

        self.send(text_data=json.dumps({'Payload': data})) # converting data to string and sending it to frontend