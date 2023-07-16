import json
from channels.generic.websocket import WebsocketConsumer

class ChatappConsummer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'msg': 'success',
            'data': 'Im here'
        }))
        # return super().connect()
