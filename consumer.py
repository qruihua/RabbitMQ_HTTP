from urllib.parse import quote
from pyrabbit.api import Client
import json


class CustomClient(Client):
    def get_custom_messages(self, vhost, qname, count=1,
                     requeue=False, truncate=None, encoding='auto'):
        vhost = quote(vhost, '')
        base_body = {'count': count, 'requeue': requeue, 'encoding': encoding}
        if truncate:
            base_body['truncate'] = truncate
        base_body['ackmode']='ack_requeue_true'
        body = json.dumps(base_body)

        qname = quote(qname, '')
        path = Client.urls['get_from_queue'] % (vhost, qname)
        messages = self.http.do_call(path, 'POST', body,
                                     headers=Client.json_headers)
        return messages

#连接
cl = CustomClient('localhost:15672', 'guest', 'guest')
#判断是否连接
cl.is_alive()
#使用vhost
cl.get_vhost('test001')
#使用channel
cl.get_exchange('test001', 'channel_001')
#使用队列
cl.get_queue('test001','queue_001')


messages=cl.get_custom_messages('test001','queue_001',count=100)
for message in messages:
    print(message['payload'])

cl.purge_queue('test001','queue_001')


