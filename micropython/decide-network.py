import time
from network import LoRa
import socket
import time
import ubinascii
import struct


available_networks = ["wifi", "lte", "lora", "sigfox"]

def appears_more_once(network_list):
    for item in network_list:
        if available_networks.count(item) > 1:
            return True
    return False

if appears_more_once(available_networks):
    raise Exception("Duplicates are in the available networks, remove duplicate networks")

networks = 0
message = "48341be6644c5eeb650561460ca6c3a39b1aebf1bbac0bcfa9c14911dce8a955"
key = "123"
hashed = "321"

def lora_send(data_to_send):
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

    print("DevEUI: " + ubinascii.hexlify(lora.mac()).decode('utf-8').upper())

    # create an OTAA authentication parameters

    app_eui = ubinascii.unhexlify('')
    app_key = ubinascii.unhexlify('')

    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    while not lora.has_joined():
        print('Not yet joined...')
        time.sleep(3)

    print("Joined network")

    # create socket to be used for LoRa communication
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    # configure data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)

    #define which port with the socket bind
    s.bind(2)

    #send some data
    s.send(data_to_send)

    s.setblocking(False)
    # get any data received...
    data = s.recv(64)
    print(data)

# disconnect from all networks to reinitialize
pybytes.disconnect()

networks = len(available_networks)

if networks == 0:
    print("No networks available")

if networks == 1:
    if "lte" in available_networks:
        pybytes.connect_lte()
        pybytes.send_signal(1, message)
        pybytes.send_signal(2, key)
        pybytes.send_signal(3, hashed)
        print("message key and hash sent by lte")
    elif "wifi" in available_networks:
        pybytes.connect_wifi()
        pybytes.send_signal(1, message)
        pybytes.send_signal(2, key)
        pybytes.send_signal(3, hashed)
        print("message key and hash sent by wifi")
    elif "sigfox" in available_networks:
        pybytes.connect_sigfox()
        pybytes.send_signal(1, message)
        pybytes.send_signal(2, key)
        pybytes.send_signal(3, hashed)
        print("message key and hash sent by sigfox")
    elif "lora" in available_networks:
        lora_send(message)
        lora_send(key)
        lora_send(hashed)
        print("message key and hash sent by lora")
    pybytes.disconnect()

if networks == 2:
    if available_networks[0] == "lte":
        pybytes.connect_lte()
        pybytes.send_signal(1, message)
        pybytes.send_signal(3, hashed)
        print("message and hash sent by lte")
    elif available_networks[0] == "wifi":
        pybytes.connect_wifi()
        pybytes.send_signal(1, message)
        pybytes.send_signal(3, hashed)
        print("message and hash sent by wifi")
    elif available_networks[0] == "sigfox":
        pybytes.connect_sigfox()
        pybytes.send_signal(1, message)
        pybytes.send_signal(3, hashed)
        print("message and hash sent by sigfox")
    elif available_networks[0] == "lora":
        lora_send(message)
        lora_send(hashed)
        print("message and hash sent by lora")

    pybytes.disconnect()

    if available_networks[1] == "lte":
        pybytes.connect_lte()
        pybytes.send_signal(2, key)
        print("key sent by lte")
    elif available_networks[1] == "wifi":
        pybytes.connect_wifi()
        pybytes.send_signal(2, key)
        print("key sent by wifi")
    elif available_networks[1] == "sigfox":
        pybytes.connect_sigfox()
        pybytes.send_signal(2, key)
        print("key sent by sigfox")
    elif available_networks[1] == "lora":
        lora_send(key)
        print("key sent by lora")

    pybytes.disconnect()

if networks == 3:
    if available_networks[0] == "lte":
        pybytes.connect_lte()
        pybytes.send_signal(1, message)
        print("message sent via lte")
    elif available_networks[0] == "wifi":
        pybytes.connect_wifi()
        pybytes.send_signal(1, message)
        print("message sent via Wifi")
    elif available_networks[0] == "sigfox":
        pybytes.connect_sigfox()
        pybytes.send_signal(1, message)
        print("message sent via sigfox")
    elif available_networks[0] == "lora":
        lora_send(message)
        print("message sent via Lora")

    pybytes.disconnect()

    if available_networks[1] == "lte":
        pybytes.connect_lte()
        pybytes.send_signal(2, key)
        print("key sent via lte")
    elif available_networks[1] == "wifi":
        pybytes.connect_wifi()
        pybytes.send_signal(2, key)
        print("key sent via wifi")
    elif available_networks[1] == "sigfox":
        pybytes.connect_sigfox()
        pybytes.send_signal(2, key)
        print("key sent via sigfox")
    elif available_networks[1] == "lora":
        lora_send(key)
        print("key sent via Lora")

    pybytes.disconnect()

    if available_networks[2] == "lte":
        pybytes.connect_lte()
        pybytes.send_signal(3, hashed)
        print("hash sent via lte")
    elif available_networks[2] == "wifi":
        pybytes.connect_wifi()
        pybytes.send_signal(3, hashed)
        print("hash sent via wifi")
    elif available_networks[2] == "sigfox":
        pybytes.connect_sigfox()
        pybytes.send_signal(3, hashed)
        print("hash sent via sigfox")
    elif available_networks[2] == "lora":
        lora_send(hashed)
        print("hash sent via lora")

    pybytes.disconnect()


if networks == 4:
    message_decode = ubinascii.unhexlify(message)
    iv = message_decode[:16]
    cipher_text_no_iv = message_decode[16:]
    iv = ubinascii.hexlify(iv).decode()
    cipher_text_no_iv = ubinascii.hexlify(cipher_text_no_iv).decode()

    if available_networks[0] == "lte":
        pybytes.connect_lte()
        pybytes.send_signal(1, cipher_text_no_iv)
        print("cipher text no iv is sent by lte: ", cipher_text_no_iv)
    elif available_networks[0] == "wifi":
        pybytes.connect_wifi()
        pybytes.send_signal(1, cipher_text_no_iv)
        print("cipher text no iv is sent by wifi: ", cipher_text_no_iv)
    elif available_networks[0] == "sigfox":
        pybytes.connect_sigfox()
        pybytes.send_signal(1, cipher_text_no_iv)
        print("cipher text no iv is sent by sigfox: ", cipher_text_no_iv)
    elif available_networks[0] == "lora":
        lora_send(cipher_text_no_iv)
        print("cipher text no iv is sent by lora: ", cipher_text_no_iv)

    pybytes.disconnect()

    if available_networks[1] == "lte":
        pybytes.connect_lte()
        pybytes.send_signal(2, key)
        print("key sent by lte")
    elif available_networks[1] == "wifi":
        pybytes.connect_wifi()
        pybytes.send_signal(2, key)
        print("key sent by wifi")
    elif available_networks[1] == "sigfox":
        pybytes.connect_sigfox()
        pybytes.send_signal(2, key)
        print("key sent by sigfox")
    elif available_networks[1] == "lora":
        lora_send(key)
        print("key sent by lora")

    pybytes.disconnect()

    if available_networks[2] == "lte":
        pybytes.connect_lte()
        pybytes.send_signal(3, hashed)
        print("hash sent by lte")
    elif available_networks[2] == "wifi":
        pybytes.connect_wifi()
        pybytes.send_signal(3, hashed)
        print("hash sent by wifi")
    elif available_networks[2] == "sigfox":
        pybytes.connect_sigfox()
        pybytes.send_signal(3, hashed)
        print("hash sent by sigfox")
    elif available_networks[2] == "lora":
        lora_send(hashed)
        print("hash sent by lora")

    pybytes.disconnect()

    if available_networks[3] == "lte":
        pybytes.connect_lte()
        pybytes.send_signal(4, iv)
        print("iv sent by lte: ", iv)
    elif available_networks[3] == "wifi":
        pybytes.connect_wifi()
        pybytes.send_signal(4, iv)
        print("iv sent by wifi: ", iv)
    elif available_networks[3] == "sigfox":
        pybytes.connect_sigfox()
        pybytes.send_signal(4, iv)
        print("iv sent by sigfox: ", iv)
    elif available_networks[3] == "lora":
        lora_send(iv)
        print("iv sent by lora: ", iv)
    
    pybytes.disconnect()