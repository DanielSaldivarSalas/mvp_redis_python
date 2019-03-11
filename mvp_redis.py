import redis
from prod_config import *

r = redis.StrictRedis(
    host =prod_redis_host,
    port = prod_redis_port,
    password=prod_redis_password
)

r.set('foo', 'bar')
value = r.get('foo')
print(value)