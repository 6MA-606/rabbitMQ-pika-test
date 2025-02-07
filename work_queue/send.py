import pika
import pika.exceptions

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
except pika.exceptions.AMQPConnectionError as e:
    print('Error:', e)
    exit(1)
finally:
    print("Connected to RabbitMQ")

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

connection.close()

print(" [x] Sent 'Hello World!'")