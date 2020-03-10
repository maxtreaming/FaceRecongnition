import time
import psycopg2

data_list = []

while(True):

    temp = 0.0
    date_time = time.localtime()
    with open("/sys/class/thermal/thermal_zone0/temp", 'r') as f:
        temp_str = f.readline()
        temp = float(temp_str) / 1000
    date_time_str = time.strftime("%Y-%m-%d %H:%M:%S", date_time)
    print("{} {}".format(date_time_str, temp))

    data_list.append((date_time_str, temp))

    if(len(data_list) == 10):
        print("Sent")

        data_list = []


    time.sleep(1)
