from pyrabbit.api import Client
#连接
cl = Client('localhost:15672', 'guest', 'guest')
#判断是否连接
cl.is_alive()
#创建vhost
cl.create_vhost('test001')
#使用vhost
cl.set_vhost_permissions('test001', 'guest', '.*', '.*', '.*')

#创建一个Channel(exchange)
cl.create_exchange('test001', 'channel_001', 'direct')

cl.get_exchange('test001', 'channel_001')

#创建队列
# 需要手动创建
# cl.create_queue('test001', 'queue_001')

#绑定 channel 和队列
cl.create_binding('test001', 'channel_001', 'queue_001', 'test_key')


#发送消息
cl.publish('test001', 'channel_001', 'test_key', 'ricky ~')



