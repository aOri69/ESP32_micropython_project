def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('MikroTik-2', 'narazdvatri')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def sd_initialise(id=2, sck=18, mosi=23, miso=19, cs=5):
    try:
        import machine
        import os
        import sdcard
        if id is not None:
            spi = machine.SPI(id, baudrate=100000, polarity=1, phase=0, sck=machine.Pin(
                sck), mosi=machine.Pin(mosi), miso=machine.Pin(miso))
        else:
            spi = machine.SPI(baudrate=100000, polarity=1, phase=0, sck=machine.Pin(
                sck), mosi=machine.Pin(mosi), miso=machine.Pin(miso))

        spi.init()
        cs = cs = machine.Pin(cs)
        print('..sucsessfuly initialised SPI interface')
        sd = sdcard.SDCard(spi, cs)
        print('..sdcard connected')
        vfs = os.VfsFat(sd)
        print('..virtual file system created')
        try:
            os.mount(vfs, '/sd')
            print('..sdcard successfuly mounted on ../sd')
        except OSError:
            print('..already mounted on ../sd')
        print(os.listdir('/sd'))
    except ImportError:
        print('..Error importing sdcard.py\n')
    except OSError:
        print('..Error while configuring sdcard connection\n..Check SDCard module is properly connected\n')
