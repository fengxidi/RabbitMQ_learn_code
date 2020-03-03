import pika
import sys

#连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()


channel.exchange_declare(exchange='logs',exchange_type='fanout')


#发送消息到交换机
message = ''.join(sys.argv[1:]) or "hello world"
channel.basic_publish(exchange='logs',
			routing_key='',
			body= message,
		
			)

print("[x] sent %s"%message)
connection.close()

