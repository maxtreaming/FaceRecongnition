from smbus import SMBus
from time import sleep
import numpy as np
import os
import select

# Pin to work with
pin_base = '/sys/class/gpio/gpio17/'


def write_once(path, value):
    with open(path, 'w') as f:
        f.write(value)

sensor_address = 0x1d
b = SMBus(1)

val = b.read_byte_data(sensor_address, 0x0F)

if val == 0b01001001:
    print("Found module")


enable_acc = 0
b.write_byte_data(sensor_address, 0x20, 0)

enable_fifo = 0b01000000
b.write_byte_data(sensor_address, 0x1F, 0)
b.write_byte_data(sensor_address, 0x1F, enable_fifo)

fifo_ctrl = 0b01000111
b.write_byte_data(sensor_address, 0x2E, 0)
b.write_byte_data(sensor_address, 0x2E, fifo_ctrl)

fifo_interrupt = 2
b.write_byte_data(sensor_address, 0x23, fifo_interrupt)

latch = 1
b.write_byte_data(sensor_address, 0x24, latch)

enable_acc = 0b01010111
b.write_byte_data(sensor_address, 0x20, enable_acc)


write_once(os.path.join(pin_base, 'direction'),
           'in')
write_once(os.path.join(pin_base, 'edge'),
           'rising')
write_once(os.path.join(pin_base, 'active_low'),
           '0')


f = open(os.path.join(pin_base, 'value'), 'r')
po = select.poll()
po.register(f, select.POLLPRI)
while 1:
    f.seek(0)
    f.read()

    event = po.poll(2000)

    if event:
        status = b.read_byte_data(sensor_address, 0x2F)

        if status & (1 << 7):

            acc_x_table = []
            acc_y_table = []
            acc_z_table = []
            for i in range(0b11111):

                long_acc_x = b.read_byte_data(sensor_address, 0x28)
                long_acc_x1 = b.read_byte_data(sensor_address, 0x29)
                long_acc_y = b.read_byte_data(sensor_address, 0x2A)
                long_acc_y1 = b.read_byte_data(sensor_address, 0x2B)
                long_acc_z = b.read_byte_data(sensor_address, 0x2C)
                long_acc_z1 = b.read_byte_data(sensor_address, 0x2D)

                acc_x_table.append(int.from_bytes([long_acc_x1, long_acc_x], byteorder='big', signed=True))
                acc_y_table.append(int.from_bytes([long_acc_y1, long_acc_y], byteorder='big', signed=True))
                acc_z_table.append(int.from_bytes([long_acc_z1, long_acc_z], byteorder='big', signed=True))

            print("Value x", sum(acc_x_table) / len(acc_x_table))
            print("Value y", sum(acc_y_table) / len(acc_y_table))
            print("Value z", sum(acc_z_table) / len(acc_z_table))


    else:
        print("Timeout")
