# from datetime import datetime, timedelta
# date = "260624"
# time_u = "114959.000"
# datetime_u = date+time_u
# utc_format = "%d%m%y%H%M%S.%f"

# # string to date conversion using strptime"
# utc_time = datetime.strptime(datetime_u,utc_format)
# ist_diff = timedelta(hours=5, minutes=30)
# # print(ist_diff)
# # print(utc_time)
# ist_time = utc_time+ist_diff
# print(ist_time)
# # print(type(utc_time))

# # print(ist_time.strftime('%d-%m-%Y %H:%M:%S'))      # reformating the datetime
# # print(type(ist_time))
# # print(ist_time.timestamp())      # convert date to epoch using timestamp()


# # unix_epoch = datetime.datetime(1970, 1, 1)       # o/p ------------1970-01-01 00:00:00
# # print(unix_epoch)





import port_fetching
import serial
import datetime_formating as fmt
class GPS:
    def __init__(self):
        pass

    def GPS():
        port = port_fetching.port()
        # print(port)
        try:
            ser = serial.Serial(port=port,baudrate=4800)
            print(ser)
        except:
            print("Not any GPS Device Available")

obj = GPS.GPS()
obj