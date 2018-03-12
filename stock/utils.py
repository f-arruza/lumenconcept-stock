import pika

from django.conf import settings

def send_message_rabbit(queue, message):
    parameters = pika.URLParameters(settings.URL_BROKER)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=queue)

    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=str(message))
    print(" [x] Message sent successfully")
    connection.close()

def receive_message_rabbit(queue, callback):
    parameters = pika.URLParameters(settings.URL_BROKER)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=queue)

    channel.basic_consume(callback,
                          queue=queue,
                          no_ack=True)

    print(' [*] Waiting for messages [' + queue + ']. To exit press CTRL+C')
    channel.start_consuming()
