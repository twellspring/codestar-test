import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'event': json.dumps(event)
    }
    return {'statusCode': 404, 'headers': {'Content-Type': 'application/json'}}
