import pika

connection = pika.BlockingConnection(parameters=pika.ConnectionParameters('localhost', port=5672))

channel = connection.channel()

channel.queue_declare('fastapi')


def callback(ch, method, properties, body):
    print(f'received body is {body}')

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='fastapi', on_message_callback=callback)
print("waiting for get message...")

channel.start_consuming()
