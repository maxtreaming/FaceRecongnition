from time import sleep

servo_address = "/sys/class/pwm/pwmchip0/pwm0/"

def write_value(address, value):
    with open(servo_address + address, 'w') as f:
        f.write(str(value))

write_value("enable", 0)
write_value("period", 20000000)
write_value("polarity", "normal")
write_value("enable", 1)

while 1:
    for i in range(600000, 2500000, 10000):
        write_value("duty_cycle", i)
        print("Up:", i)
        sleep(0.005)

    for i in range(2500000, 600000, -10000):
        write_value("duty_cycle", i)
        print("Down:", i)
        sleep(0.005)


