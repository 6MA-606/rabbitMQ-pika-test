# RabbitMQ - Demo

<div align="center">
<a  href="https://www.rabbitmq.com/">
<img src="https://www.rabbitmq.com/img/rabbitmq-logo-with-name.svg" alt="RabbitMQ" width="300px" height="200px" />
</a>

This repository contains a simple demo of RabbitMQ using Python with the `pika` library.
</div>

# What is RabbitMQ?

[RabbitMQ](https://www.rabbitmq.com/) is an open-source message broker that facilitates communication between distributed applications by implementing the `Advanced Message Queuing Protocol (AMQP)`. It acts as an intermediary for messaging, enabling applications to send and receive messages asynchronously, improving scalability, reliability, and decoupling between services. RabbitMQ supports various messaging patterns, including publish/subscribe, request/reply, and work queues, making it widely used in microservices architectures, event-driven systems, and background job processing. It provides features like message persistence, routing, acknowledgments, and clustering, ensuring efficient and fault-tolerant message delivery across different systems.

# Get Started

This demo implements a simple producer-consumer model using RabbitMQ. Using the `pika` library, we create a producer that sends messages to a queue and a consumer that receives messages from the queue.

Refer to the [RabbitMQ tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python) for more information.

## Installation

To install the required dependencies, run the following command:

```bash
python -m pip install pika --upgrade
```

## Deploy RabbitMQ Server

To deploy a RabbitMQ server using Docker, run the following command:

```bash
# latest RabbitMQ 4.0.x
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management
```

Or using Docker Compose:

`compose.yml`:

```yaml
version: '3.8'

services:
  rabbitmq:
    image: "rabbitmq:4.0-management"
    container_name: "rabbitmq"
    ports:
      - "15672:15672"   # RabbitMQ Management UI
      - "5672:5672"     # RabbitMQ AMQP Protocol
    volumes:
      - "rabbitmq_data:/var/lib/rabbitmq"
      - "rabbitmq_logs:/var/log/rabbitmq"
    environment:
      RABBITMQ_DEFAULT_USER: guest
      RABBITMQ_DEFAULT_PASS: guest
      RABBITMQ_DEFAULT_VHOST: /

volumes:
  rabbitmq_data:
  rabbitmq_logs:
```

Run the following command to deploy the RabbitMQ server:

```bash
docker-compose -f /path/to/compose.yml up
```

<br />

> You can access management UI at [http://localhost:15672](http://localhost:15672) with the default credentials `guest:guest` (Username: `guest`, Password: `guest`).