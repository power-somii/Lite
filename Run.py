import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Junaid import Subscription
    Subscription()
else:
    print('\n Checking Server Please Wait.....')
    os.system('exit')
