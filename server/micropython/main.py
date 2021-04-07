from crypto import AES
import crypto
import uhashlib
import ubinascii
import time
import machine

password = "anypasswi38jsdjfjfdsjord".encode()
key = uhashlib.sha256(password).digest() # 32byte key generated from sha256 since AES requrires 16 24 or 32 bytes

for i in range(5):

        iv = crypto.getrandbits(128) # Random iv

        message = "[" + str(round(machine.rng()/10000)) + "," + str(round(machine.rng()/10000)) + "," + str(round(machine.rng()/10000)) + "]"

        # HASHING DATA For integrity
        data_hash = uhashlib.sha256(message)
        data_hash_hex = ubinascii.hexlify(data_hash.digest()).decode()

        while len(message) % 16 != 0:
                message = message + " "

        cipher = AES(key, AES.MODE_CFB, iv)

        new_iv = ubinascii.hexlify(iv).decode()
        new_msg = ubinascii.hexlify(cipher.encrypt(message)).decode()

        enc_msg = new_iv + new_msg

        # Data sent via pybytes. POST Request made to server to receive data
        pybytes.send_signal(1, str(enc_msg)) 
        time.sleep(3)
        key_hex = ubinascii.hexlify(key).decode()

        pybytes.send_signal(2, str(key_hex))
        time.sleep(3)

        #send hash of data via pybytes
        pybytes.send_signal(3, str(data_hash_hex))
        #print for information

        print("Hash of data is: ", data_hash_hex)
        print("data sent encrypted string is: ", enc_msg)
        print("hashed key sent is: ", key_hex)
        time.sleep(10)

# To decrypt data after it has been sent somewhere
#orig_data = ubinascii.unhexlify(enc_msg)

#print(orig_data)

#cipher = AES(key, AES.MODE_CFB, orig_data[:16]) # To decrypt orginal data
#dec_msg = cipher.decrypt(orig_data[16:])
#print(dec_msg.rstrip().decode())  # rstrip to remove extra padding and decode to turn from binary to text