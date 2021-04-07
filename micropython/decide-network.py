import time

available_networks = ["lte", "wifi"]#, "sigfox", "lora", "bluetooth"]

networks = 0
message = "hello"
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
print(networks)

if networks == 0:
    print("No networks available")

if networks == 1:
    if "lte" in available_networks:
        pybytes.connect_lte()
        pybytes.send_signal(1, message)
        pybytes.send_signal(2, key)
        pybytes.send_signal(3, hashed)
    elif "wifi" in available_networks:
        pybytes.connect_wifi()
        pybytes.send_signal(1, message)
        pybytes.send_signal(2, key)
        pybytes.send_signal(3, hashed)
    elif "sigfox" in available_networks:
        pybytes.connect_sigfox()
        pybytes.send_signal(1, message)
        pybytes.send_signal(2, key)
        pybytes.send_signal(3, hashed)
    elif "lora" in available_networks:
        lora_send(message)
        lora_send(key)
        lora_send(hashed)
    #if "bluetooth" in available_networks:
    pybytes.disconnect()

if networks == 2:
    if available_networks[0] == "lte"
        pybytes.connect_lte()
        pybytes.send_signal(1, message)
        pybytes.send_signal(3, hashed)
    elif available_networks[0] == "wifi"
        pybytes.connect_wifi()
        pybytes.send_signal(1, message)
        pybytes.send_signal(3, hashed)
    elif available_networks[0] == "sigfox"
        pybytes.connect_lte()
        pybytes.send_signal(1, message)
        pybytes.send_signal(3, hashed)
    elif available_networks[0] == "lora"
        lora_send(message)
        lora_send(hashed)
    pybytes.disconnect()
    if available_networks[1] == "lte"
        pybytes.connect_lte()
        pybytes.send_signal(2, key)
    elif available_networks[1] == "wifi"
        pybytes.connect_wifi()
        pybytes.send_signal(2, key)
    elif available_networks[1] == "sigfox"
        pybytes.connect_lte()
        pybytes.send_signal(2, key)
    elif available_networks[1] == "lora"
        lora_send(key)
    pybytes.disconnect()

if networks >= 3:
    if available_networks[0] == "lte"
        pybytes.connect_lte()
        pybytes.send_signal(1, message)
    elif available_networks[0] == "wifi"
        pybytes.connect_wifi()
        pybytes.send_signal(1, message)
    elif available_networks[0] == "sigfox"
        pybytes.connect_lte()
        pybytes.send_signal(1, message)
    elif available_networks[0] == "lora"
        lora_send(message)
    pybytes.disconnect()
    if available_networks[1] == "lte"
        pybytes.connect_lte()
        pybytes.send_signal(2, key)
    elif available_networks[1] == "wifi"
        pybytes.connect_wifi()
        pybytes.send_signal(2, key)
    elif available_networks[1] == "sigfox"
        pybytes.connect_lte()
        pybytes.send_signal(2, key)
    elif available_networks[1] == "lora"
        lora_send(key)
    pybytes.disconnect()
    if available_networks[2] == "lte"
        pybytes.connect_lte()
        pybytes.send_signal(3, hashed)
    elif available_networks[2] == "wifi"
        pybytes.connect_wifi()
        pybytes.send_signal(3, hashed)
    elif available_networks[2] == "sigfox"
        pybytes.connect_lte()
        pybytes.send_signal(3, hashed)
    elif available_networks[2] == "lora"
        lora_send(hashed)
    pybytes.disconnect()



