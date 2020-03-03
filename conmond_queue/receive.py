import pika

#创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

#指定队列
channel.queue_declare(queue='hello')


def callback(ch, method, propertites, body):
	print("[x] Receive {}".format(body))

channel.basic_consume('hello', callback)

print('waiting for message ')
channel.start_consuming()
