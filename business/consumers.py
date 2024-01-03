import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Availability

class CheckInOutConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data['action']
        business_id = data['business_id']
        availability = await self.get_availability(business_id)

        if action == 'check_in':
            availability.available_tables -= 1
        elif action == 'check_out':
            availability.available_tables += 1

        availability.save()

        await self.send(text_data=json.dumps({
            'action': action,
            'availability': availability.available_tables,
        }))

    @sync_to_async
    def get_availability(self, business_id):
        return Availability.objects.get(business_id=business_id)
