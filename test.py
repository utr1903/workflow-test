import os
import json


secret = os.getenv("TEST_SECRET") + " TEST"
print(type(secret))
print(secret)

infos = json.loads("{}".format(secret))
print(type(infos))
print(infos)

for info in infos:
    print(type(info))
    print(info)

    x = info["organizationName"]
    print(x)
