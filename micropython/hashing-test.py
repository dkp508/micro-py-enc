import pycom
import time
import uhashlib
import ubinascii

pycom.heartbeat(False)

data = [100, 400, 300, 200]
data_string = ''.join(str(m) for m in data)


data_hash = uhashlib.sha256(data_string)
data_hash_hex = ubinascii.hexlify(data_hash.digest())

print(data_hash_hex)

