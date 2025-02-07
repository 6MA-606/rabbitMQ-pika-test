import pika, sys, os, random, math, time

def send_task(task_number, channel):
    duration = math.ceil(random.random() * 2)
    message = f"No. {task_number + 1} | Task ({duration}s)"
    channel.basic_publish(exchange='',
                          routing_key='work_queue',
                          body=message)
    print(f" [x] Sent {message}")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='work_queue')

    task_amount = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    for i in range(task_amount):
        send_task(i, channel)
        # time.sleep(1)

    connection.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)