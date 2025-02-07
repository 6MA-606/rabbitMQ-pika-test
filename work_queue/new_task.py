import pika, sys

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
except pika.exceptions.AMQPConnectionError as e:
    print('Error:', e)
    exit(1)
finally:
    print("Connected to RabbitMQ")

channel = connection.channel()

channel.queue_declare(queue='work_queue')

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='work_queue',
                      body=message)
print(f" [x] Sent {message}")