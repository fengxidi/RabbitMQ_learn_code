import pika
import sys

#连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()


#创建消息队列

channel.queue_declare(queue='task_queue',durable=True)

#发送消息到消息队列
message = ''.join(sys.argv[1:])
channel.basic_publish(exchange='',
			routing_key='hello',
			body= message,
			properties=pika.BasicProperties(delivery_mode=2),
			)

print("[x] sent %s"%message)
connection.close()

