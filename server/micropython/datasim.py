import time
import machine
import uhashlib
import ubinascii

for i in range(5):
    sim_data = "[" + str(round(machine.rng()/10000)) + "," + str(round(machine.rng()/10000)) + "," + str(round(machine.rng()/10000)) + "]"
    print(sim_data)
    
    data_hash = uhashlib.sha256(sim_data)
    data_hash_hex = ubinascii.hexlify(data_hash.digest()).decode()

    print(data_hash_hex)
    time.sleep(1)