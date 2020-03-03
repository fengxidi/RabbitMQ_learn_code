import pika
import sys


#创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()


#创建交换机
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

#创建临时队列
result = channel.queue_declare('',exclusive=True)

queue_name = result.method.queue


severities = sys.argv[1:]

if not severities:
	print(">>",sys.stderr, "Usage: %s [info] [warning] [error]"%(sys.argv[0]))
	sys.exit(1)

for severity in severities:

#绑定交换机和队列
	channel.queue_bind(exchange='direct_logs',
				queue=queue_name,
				routing_key=severity)


def callback(ch, method, propertites, body):
	print("[x] {} >>: {}".format(method.routing_key, body))
	
	ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue_name, callback)

print('waiting for message ')
channel.start_consuming()
