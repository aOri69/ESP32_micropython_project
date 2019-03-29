# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
webrepl.start()
#####################################################
from basic_functions import do_connect, sd_initialise
# WiFi Connection
do_connect()
# SD Card init on 5,18,19,23 pins using VSPI
sd_initialise()

