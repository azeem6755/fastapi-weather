import redis
import json


redis_client = redis.Redis(host='localhost', port=6379, db=0)


def get_data_from_cache(location: str, start_date: str|None, end_date: str|None):
    item_id = location
    item_id = item_id + "_" + start_date if start_date else item_id
    item_id = item_id + "_" + end_date if end_date else item_id

    cached_item = redis_client.get(item_id)
    if cached_item:
        return {"item_id": item_id, "cached": True, "data": json.loads(cached_item.decode('utf-8'))}
    return None


def store_data_in_cache(location:str, start_date: str|None, end_date: str|None, data: dict):
    item_id = location
    item_id = item_id + "_" + start_date if start_date else item_id
    item_id = item_id + "_" + end_date if end_date else item_id

    json_data = json.dumps(data)

    redis_client.setex(item_id, 3600, json_data)

    return {'item_id': item_id, 'cached': False, 'data': data}
