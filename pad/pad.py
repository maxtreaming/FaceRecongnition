import struct

EVENT_BUTTON = 0x01
EVENT_AXIS = 0x02
EVENT_INIT = 0x80

with open('/dev/input/js0', 'rb') as f:
    while 1:
        data = f.read(8)

        unpacked = struct.unpack('IhBB', data)

        if EVENT_BUTTON == unpacked[2]:
            print("Button:", unpacked[3], "Value:", unpacked[1])
            
        if EVENT_AXIS == unpacked[2] and 0 == unpacked[3]:
            print("Axis:", unpacked[3], "Value:", unpacked[1])

        

