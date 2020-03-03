import pika
import time

#创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

#指定队列
channel.queue_declare(queue='task_qqueue',durable=True)


def callback(ch, method, propertites, body):
	print("[x] Receive {}".format(body))
	time.sleep(body.count(b'.'))
	time.sleep(10)
	print("[x] Done")
	ch.basic_ack(delivery_tag = method.delivery_tag)
channel.basic_qos(prefetch_count=1)
channel.basic_consume('hello', callback)

print('waiting for message ')
channel.start_consuming()
