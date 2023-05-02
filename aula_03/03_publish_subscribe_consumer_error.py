import pika
import sys
import os
import time


def main():
    # Create a connection to the RabbitMQ server running on the local machine
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare a queue to consume messages from
    result = channel.queue_declare(
        queue='', 
        exclusive=True
    )

    # Define exchange and queue name s
    exchange_name = 'direct_logs'
    queue_name = result.method.queue

    # Declare exchange
    channel.exchange_declare(
        exchange=exchange_name,
        exchange_type='direct'
    )

    # Declare queue bindings
    severities = ['error']
    
    for severity in severities:
        channel.queue_bind(
            exchange=exchange_name,
            queue=queue_name,
            routing_key=severity
        )
 
    # Define a callback function to handle incoming messages
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        print(f"{method.routing_key}")

        with open('logs/direct_log_errors.txt', 'a') as f:
            f.write(f'{body} \n')
        
        print('[X] Done.')




    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    # Start consuming messages from the queue
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')

        # Attempt to exit gracefully
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)