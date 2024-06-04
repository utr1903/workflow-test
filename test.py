import os
import json


# infos = json.loads(json.loads(os.getenv("TEST_SECRET")))
infos = json.loads(os.getenv("TEST_SECRET"))
print(type(infos))
print(infos)

for info in infos:
    print(type(info))
    print(info)

    x = info["organizationName"]
    print(x)
