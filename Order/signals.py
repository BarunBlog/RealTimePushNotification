from django.db.models.signals import post_save
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Order
import json



@receiver(post_save, sender=Order)
def review_created(sender, **kwargs):

        the_instance = kwargs['instance']
        if 'status' in kwargs['update_fields']:
            channel_layer = get_channel_layer()
            print('updated')
            async_to_sync(channel_layer.group_send)(
            'id_%s' % the_instance.id, { # group name
                'type': 'order_status', # custom method name
                'message': json.dumps('Order status changed')
                
                }
            )
