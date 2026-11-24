import pika
from fastapi import FastAPI

app = FastAPI()

connection = pika.BlockingConnection(parameters=pika.ConnectionParameters('localhost', port=5672))

channel = connection.channel()

channel.queue_declare('fastapi')

@app.post('/jobs/reports')
def send_job():
    channel.basic_publish(exchange='', routing_key='fastapi', body="this is test 12body")
    print("task sent!")
    # connection.close()
