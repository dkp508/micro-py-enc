from flask import json
from flask import request
from flask import Flask
import binascii
import hashlib
from Crypto.Cipher import AES

app = Flask(__name__)

data = ""
enc_data_and_key = []
hash_of_data = ""
dec_data_list = []

def decrypt_data(string_to_decode, key):
    orig_data = binascii.unhexlify(string_to_decode)
    orig_key = binascii.unhexlify(key)
    iv = orig_data[:16]
    cryptostring = orig_data[16:]
    cipher = AES.new(orig_key, AES.MODE_CFB, iv) # To decrypt
    dec_msg = cipher.decrypt(cryptostring)
    dec_data = dec_msg.rstrip().decode()
    dec_data_list.append(dec_data)
    print("Decrypted Message: ", dec_data)  # rstrip to remove extra padding and decode to turn from binary to text

def verify_hash(hash_to_verify, data_dec):
    #compute hash of data received
    new_data_hash = hashlib.sha256(data_dec.encode())
    new_data_hash_hex = binascii.hexlify(new_data_hash.digest()).decode()
    #compare to hash received before being sent
    if hash_to_verify == new_data_hash_hex:
        print("Hash Matches, data is the same. Hash before:" + hash_to_verify + "Hash after:" + new_data_hash_hex + "\n\n")
    else:
        print("Hash does not match, data is not the same. Hash before:" + hash_to_verify + "Hash after:" + new_data_hash_hex + "\n\n")
    dec_data_list.clear()

#default route at /
@app.route("/")
def hello():
    return "Default route"

#route at /pybytes to accept POST requests
@app.route("/pybytes", methods=["POST"])
def get_signal():
    if request.headers["Content-Type"] == "application/json":
        data = json.dumps(request.json)
        data_list = json.loads(data)
        if data_list["signal"] == "1":
            print("Encrypted String Is: ", data_list["payload"])
            enc_data_and_key.append(data_list["payload"])
        elif data_list["signal"] == "2":
            print("Hashed Key is: ", data_list["payload"], len(data_list["payload"]))
            enc_data_and_key.append(data_list["payload"])
        elif data_list["signal"] == "3":
            print("Hash of data is: ", data_list["payload"])
            hash_of_data = data_list["payload"]
            verify_hash(hash_of_data, dec_data_list[0])
        if len(enc_data_and_key) >= 2 and len(enc_data_and_key) % 2 == 0:
            if len(enc_data_and_key[1]) == 64:
                decrypt_data(enc_data_and_key[0], enc_data_and_key[1])
                enc_data_and_key.clear()
            else:
                print("Error, items received in wrong order or incorrect length")
        #print(enc_data_and_key)
        return data
        


if __name__ == '__main__':
    app.run()

