import pika
import time

#创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()


#创建交换机
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

#创建临时队列
result = channel.queue_declare('',exclusive=True)

queue_name = result.method.queue

#绑定交换机和队列
channel.queue_bind(exchange='logs',
			queue=queue_name)


def callback(ch, method, propertites, body):
	print("[x] Receive {}".format(body))
	print("[x] Done")
	ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue_name, callback)

print('waiting for message ')
channel.start_consuming()
