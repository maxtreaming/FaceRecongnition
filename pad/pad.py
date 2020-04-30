import struct

servo_address = "/sys/class/pwm/pwmchip0/pwm0/"
x_min = -32768.0
x_max = 32767.0

s_min = 600000.0
s_max = 2500000.0

f_a = (s_max - s_min) / (x_max - x_min)
f_b = s_max - f_a * x_max
def get_servo_value(value):
    return int(f_a * value + f_b)

EVENT_BUTTON = 0x01
EVENT_AXIS = 0x02
EVENT_INIT = 0x80

def write_value(address, value):
    with open(servo_address + address, 'w') as f:
        f.write(str(value))

write_value("period", 20000000)
write_value("polarity", "normal")
write_value("enable", 1)

with open('/dev/input/js0', 'rb') as f:
    while 1:
        data = f.read(8)

        unpacked = struct.unpack('IhBB', data)

        if EVENT_BUTTON == unpacked[2]:
            print("Button:", unpacked[3], "Value:", unpacked[1])
            
        if EVENT_AXIS == unpacked[2] and 0 == unpacked[3]:
            print("Axis:", unpacked[3], "Value:", unpacked[1])
            write_value("duty_cycle", get_servo_value(unpacked[1]))
