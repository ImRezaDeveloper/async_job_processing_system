from typing import Annotated
import pika
from fastapi import Depends, FastAPI
from db.database import Base
from db.database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(bind=engine)
connection = pika.BlockingConnection(parameters=pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

@app.post('/jobs/reports')
def send_job():
    channel.queue_declare('fastapi')
    channel.basic_publish(exchange='', routing_key='fastapi', body="this is test 12 body")
    print("task sent!")
    return "task sent"
    # connection.close()

# send_job()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

db_dependecies = Annotated[Session, Depends(get_db)]