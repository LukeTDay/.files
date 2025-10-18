import json
import sys
import time

x = 0
while True:
    if x > 6: 
        x = 0
    output = {"alt": str(x)}
    print(json.dumps(output))
    sys.stdout.flush()
    x += 1                       
    time.sleep(1)
