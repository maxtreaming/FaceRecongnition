import time
import psycopg2

data_list = []

def getTemp():
    with open("/sys/class/thermal/thermal_zone0/temp", 'r') as f:
        temp_str = f.readline()
        temp = float(temp_str) / 1000
        return temp

def getTime():
    date_time = time.localtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", date_time)

def sendToDb(list_of_records):
    try:
       connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="192.168.0.101",
                                      port="5432",
                                      database="postgres")
       cursor = connection.cursor()

       postgres_insert_query = """ INSERT INTO raspberrypitemperature (time, value) VALUES (%s,%s)"""

       for i, element in enumerate(list_of_records):
            cursor.execute(postgres_insert_query, element)

       connection.commit()
       count = cursor.rowcount
       print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



while 1:
    data_to_send = []
    for i in range(10):
        data_to_send.append((getTime(), getTemp()))
        time.sleep(1)

    sendToDb(data_to_send)
