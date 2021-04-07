#import pycom
#import time
import uhashlib
import ubinascii

#pycom.heartbeat(False)

#data = [100, 400, 300, 200]
#data_string = ''.join(str(m) for m in data)
message = b"[100,200,300,400]"

data_hash = uhashlib.sha256(message)
data_hash_hex = ubinascii.hexlify(data_hash.digest()).decode()

print(data_hash_hex)

