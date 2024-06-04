import os
import json

try:
    infos = accounts = json.loads(os.getenv("TEST_SECRET"))
    print(infos)
    
    for info in infos:
      print(info)
      print(info["organizationName"])
        
except Exception as e:
    print(e)
