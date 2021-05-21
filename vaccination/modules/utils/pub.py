import redis
import time

andhra_pradesh = redis.Redis(host='redis', port=6379, db=0)

for i in range(20):
    
    andhra_pradesh.publish('URL', 'URL '+str(i))
    time.sleep(2)

