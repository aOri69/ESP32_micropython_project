def do_connect(ssid = "rt-ax88u", passphrase = "narazdvatri"):
    import network
    import time
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('...connecting to network ' + ssid)
        wlan.connect(ssid, passphrase)
        t = time.time()
        while not wlan.isconnected():
            if time.time() - t > 10:
                print('...error connecting timeout ' + ssid)
                break
        print('...network config on: ' + ssid + '\n', wlan.ifconfig())
    else:
        print('...already connected on: ' + ssid + '\n', wlan.ifconfig())
    