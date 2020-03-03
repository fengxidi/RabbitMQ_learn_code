import pika

#连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()


#创建消息队列

channel.queue_declare(queue='hello')

#发送消息到消息队列

channel.basic_publish(exchange='',
			routing_key='hello',
			body='hello world'
			)

print("[x] sent 'hello world")
connection.close()
