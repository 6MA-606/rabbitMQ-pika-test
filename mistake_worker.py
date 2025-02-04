#!/usr/bin/env python
import pika, sys, os, time, re, random

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='work_queue')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")

        # Simulate a mistake
        if random.random() < 0.2:
            print(" [x] Mistake made")
            exit(1)
        else:
            ch.basic_ack(delivery_tag = method.delivery_tag)

        time.sleep(int(re.findall(r'(\d+)', body.decode())[-1]))
        print(" [x] Done")


    channel.basic_consume(queue='work_queue', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)