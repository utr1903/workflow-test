import os
import json

try:
    secret = os.getenv("TEST_SECRET")
    print(type(secret))

    infos = accounts = json.loads(secret)
    print(type(infos))
    print(infos)

    for key, value in infos.items():
        print(type(key))
        print(key)
        print(type(value))
        print(value)

except Exception as e:
    print(e)
