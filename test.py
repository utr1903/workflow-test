import os
import json

try:
    x = json.loads(os.getenv("TEST_SECRET"))
    print(x)
except Exception as e:
    print(e)
