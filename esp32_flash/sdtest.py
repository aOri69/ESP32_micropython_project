# Test for sdcard block protocol
# Peter hinch 30th Jan 2016
import os, machine, utime

def sdtest():
    print('Filesystem check')
    print(os.listdir('/sd'))
    
    line = 'abcdefghijklmnopqrstuvwxyz\n'
    lines = line * 20000 # 540000 chars
    short = '1234567890\n'

    fn = '/sd/rats.txt'
    print()
    print('Multiple block read/write')
    with open(fn,'w') as f:
        start = utime.ticks_ms()
        n = f.write(lines)
        print(n, 'bytes written', utime.ticks_diff(utime.ticks_ms(), start))
        start = utime.ticks_ms()
        n = f.write(short)
        print(n, 'bytes written', utime.ticks_diff(utime.ticks_ms(), start))
        start = utime.ticks_ms()
        n = f.write(lines)
        print(n, 'bytes written', utime.ticks_diff(utime.ticks_ms(), start))
    
    start = utime.ticks_ms()
    with open(fn,'r') as f:
        result1 = f.read()
        print(len(result1), 'bytes read', utime.ticks_diff(utime.ticks_ms(), start))

    fn = '/sd/rats1.txt'
    print()
    print('Single block read/write')
    
    start = utime.ticks_ms()
    with open(fn,'w') as f:
        n = f.write(short) # one block
        print(n, 'bytes written', utime.ticks_diff(utime.ticks_ms(), start))
    
    start = utime.ticks_ms()
    with open(fn,'r') as f:
        result2 = f.read()
        print(len(result2), 'bytes read', utime.ticks_diff(utime.ticks_ms(), start))


    print()
    print('Verifying data read back')
    success = True
    if result1 == ''.join((lines, short, lines)):
        print('Large file Pass')
    else:
        print('Large file Fail')
        success = False
    if result2 == short:
        print('Small file Pass')
    else:
        print('Small file Fail')
        success = False
    print()
    print('Tests', 'passed' if success else 'failed')
