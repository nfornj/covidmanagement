
import redis
import time


celery= redis.StrictRedis('redis', 6379, charset="utf-8", decode_responses=True)
p = celery.pubsub()
p.psubscribe('response')
count = 0
for new_message in p.listen():
        print(new_message)

