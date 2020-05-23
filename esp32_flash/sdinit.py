def sd_initialise(id=2, baudrate=80000000, polarity=0, phase=0, bits=8, firstbit=0, sck=18, mosi=23, miso=19, cs=4):
    try:
        import machine
        import sdcard
        import os
        spi = machine.SPI(id, baudrate=baudrate, polarity=polarity, phase=phase, 
                          bits = bits, firstbit = firstbit, sck=machine.Pin(sck),
                          mosi=machine.Pin(mosi), miso=machine.Pin(miso))
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