import pika
import sys

#连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()


channel.exchange_declare(exchange='topic_logs',exchange_type='topic')


#发送消息到交换机
severity = sys.argv[1] if len(sys.argv)> 1 else 'anonymous.info'
message = ''.join(sys.argv[2:]) or "hello world"
channel.basic_publish(exchange='topic_logs',
			routing_key=severity,
			body= message,
		
			)

print("[x] sent %s >>: %s"%(severity,message))
connection.close()
