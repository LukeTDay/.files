import json
import sys
import time

x = 0
while True:
    if x > 3: 
        x = 0

    if x == 0:
        cls = "firefox"
    elif x == 1:
        cls = "github"
    elif x == 2:
        cls = "youtube"
    elif x==3:
        cls = "manga"
    output = {
        "alt": str(x),
        "class" : cls
    }
    print(json.dumps(output))
    sys.stdout.flush()
    x += 1                       
    time.sleep(1)
