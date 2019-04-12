
    def getRedisConnection():
        host = settings.REDIS_HOST
        port = settings.REDIS_PORT
        db = settings.REDIS_DB
        for i in [0, 1, 2]:
            try:
                con = redis.Redis(host=host, port=port, db=db, socket_keepalive=True, socket_timeout=3)
                return con
            except:
                print("Redis connection failed! Retyring %d.." % i)
                if i == 2:
                    print(traceback.format_exc())
                    print("Redis connection failed 3 times. Giving up..")
                    raise

    def get_value(key_type, key, connection=None):
        try:
            if connection is None:
                connection = RedisUtils.getRedisConnection()
            key_type = ' '.join(key_type.split())
            key = ' '.join(key.split())
            mapping = connection.get(key_type).decode('utf-8')
            query_mapping = json.loads(mapping)
            return query_mapping[key]
        except Exception as e:
            print(e)
            return None

    def redis_keys():
        try:
            connection = RedisUtils.getRedisConnection()
            return connection.keys()
        except Exception as e:
            print(e)
            return None

    def redis_append(key_type, key, value, connection=None):
        if connection is None:
            connection = RedisUtils.getRedisConnection()
        key_type = ' '.join(key_type.split())
        key = ' '.join(key.split())
        mapping = connection.get(str.encode(key_type)).decode('utf-8')
        mapping = json.loads(mapping)
        try:
            mapping = ast.literal_eval(mapping)
        except Exception as e:
            print(e)
            pass
        try:
            value = ast.literal_eval(value)
        except Exception as e:
            print(e)
            pass
        print(type(mapping))
        mapping[key] = value
        data = json.dumps(mapping)
        connection.set(key_type, data)
        response = {'status': 'success', 'response': mapping}
        return response

    def redis_remove(key_type, key, connection=None):
        if connection is None:
            connection = RedisUtils.getRedisConnection()
        key_type = ' '.join(key_type.split())
        mapping = connection.get(key_type).decode('utf-8')
        mapping = json.loads(mapping)
        key = ' '.join(key.split())
        if key in mapping:
            del mapping[key]
            data = json.dumps(mapping)
            connection.set(key_type, data)
            response = {'status': 'success', 'response': mapping}
            return response
        else:
            response = {'status': 'failed', 'response': "key not in key_type mapping"}
            return response

    def redis_delete(key_type, connection=None):
        if connection is None:
            connection = RedisUtils.getRedisConnection()
        key_type = ' '.join(key_type.split())
        if str.encode(key_type) in connection.keys():
            connection.delete(key_type)
            q = connection.keys()
            q = str(q)
            response = {'status': 'success', 'response': {"keys": q}}
            return response
        else:
            response = {'status': 'failed', 'response': "key_type not in redisdb"}
            return response

    def redis_insert(key_type, value, connection=None):
        if connection is None:
            connection = RedisUtils.getRedisConnection()
        value_json = json.dumps(value)
        key_type = ' '.join(key_type.split())
        connection.set(key_type, value_json)
        response = {'status': 'success', 'response': {key_type: value}}
        return response



