import os
import json


secret = os.getenv("TEST_SECRET")
print(type(secret))
print(secret)

infos = json.loads(secret)
print(type(infos))
print(infos)

infos = json.loads(
    '[{"organizationName":"MY ORG","accountId":"123","accountApiKey":"XXX","accountRegion":"AA"}]'
)
print(type(infos))
print(infos)

for key, value in infos.items():
    print(type(key))
    print(key)
    print(type(value))
    print(value)
