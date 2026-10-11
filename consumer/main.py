#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='some-rabbit')
)

channel = connection.channel()

channel.queue_declare(
    queue='hello',
    durable=True,
    arguments={'x-queue-type': 'quorum'}
)

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}", flush=True)

channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True
)

print(" [*] Waiting for messages. To exit press CTRL+C", flush=True)

channel.start_consuming()