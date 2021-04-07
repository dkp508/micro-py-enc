from crypto import AES
import crypto
import uhashlib
import ubinascii

password = "anypassword".encode()
key = uhashlib.sha256(password).digest() # 32byte key generated from sha256 since AES requrires 16 24 or 32 bytes

iv = crypto.getrandbits(128) # Random iv

message = b"hello"

while len(message) % 16 != 0:
        message = message + " "

cipher = AES(key, AES.MODE_CFB, iv)

new_iv = ubinascii.hexlify(iv).decode()
new_msg = ubinascii.hexlify(cipher.encrypt(message)).decode()

enc_msg = new_iv + new_msg

# Data sent via pybytes. POST Request made to server to receive data
pybytes.send_signal(1, str(enc_msg)) 

key_hex = ubinascii.hexlify(key).decode()

pybytes.send_signal(2, str(key_hex))


#print for information

print("data sent encrypted string is: ", enc_msg)
print("hashed key sent is: ", key_hex)

# To decrypt data after it has been sent somewhere
#orig_data = ubinascii.unhexlify(enc_msg)

#print(orig_data)

#cipher = AES(key, AES.MODE_CFB, orig_data[:16]) # To decrypt orginal data
#dec_msg = cipher.decrypt(orig_data[16:])
#print(dec_msg.rstrip().decode())  # rstrip to remove extra padding and decode to turn from binary to text