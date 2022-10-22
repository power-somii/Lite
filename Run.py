print("\33[1;32mChecking Server Please Wait")

import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Syed import Subscription
    Subscription()
elif bit == '32bit':
    from Syed32 import main
    main()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.system('exit')
