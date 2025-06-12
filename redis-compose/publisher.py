from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()
r = redis.Redis(host="redis", port=6379, db=0)


class Message(BaseModel):
    text: str


@app.post("/publish")
def publish_message(message: Message):
    r.publish("Main_Channel", message.text)
    return {"status": "Message published!"}
