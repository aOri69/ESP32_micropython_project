# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
#####################################################
import wlan
# import sd
# WiFi Connection
wlan.do_connect()
# SD Card init on 4,18,19,23 pins using VSPI
# sd.sd_initialise()

