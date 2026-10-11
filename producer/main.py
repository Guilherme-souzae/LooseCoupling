#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='some-rabbit')
)
channel = connection.channel()

channel.queue_declare(
    queue='hello',
    durable=True,
    arguments={'x-queue-type': 'quorum'}
)

counter = 0

while True:
    counter += 1

    message = f'Hello World! #{counter}'

    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=message
    )

    print(f" [x] Sent '{message}'", flush=True)

    time.sleep(1)