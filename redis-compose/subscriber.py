import redis

r = redis.Redis(host="redis", port=6379, db=0)
pubsub = r.pubsub()
pubsub.subscribe("Main_Channel")

for message in pubsub.listen():
    if message["type"] == "message":
        print(f"Got new message: {message['data'].decode()}")
