import redis
from weixintest.core import config, constants
r_cache = redis.StrictRedis(**config.REDIS_PARAMS)

def get_access_token():
    return r_cache.get(constants.REDIS_ACCESS_TOKEN)

if __name__ == '__main__':
    print get_access_token()
