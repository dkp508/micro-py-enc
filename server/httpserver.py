from flask import json
from flask import request
from flask import Flask
import binascii
import hashlib
from Crypto.Cipher import AES

app = Flask(__name__)

data = ""
enc_data_and_key = []

def decrypt_data(string_to_decode, key):
    orig_data = binascii.unhexlify(string_to_decode)
    orig_key = binascii.unhexlify(key)
    iv = orig_data[:16]
    cryptostring = orig_data[16:]
    cipher = AES.new(orig_key, AES.MODE_CFB, iv) # To decrypt
    dec_msg = cipher.decrypt(cryptostring)
    print("Decrypted Message: ", dec_msg.rstrip().decode())  # rstrip to remove extra padding and decode to turn from binary to text

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
        if data_list["signal"] == "7":
            print("Encrypted String Is: ", data_list["payload"])
            enc_data_and_key.append(data_list["payload"])
        elif data_list["signal"] == "8":
            print("Hashed Key is: ", data_list["payload"])
            enc_data_and_key.append(data_list["payload"])
        if len(enc_data_and_key) % 2 == 0:
            if len(enc_data_and_key[0]) == 128:
                decrypt_data(enc_data_and_key[0], enc_data_and_key[1])
                enc_data_and_key.clear()
            else:
                print("Error, items received in wrong order or incorrect length")
        print(enc_data_and_key)
        return data
        


if __name__ == '__main__':
    app.run()

