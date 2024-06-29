# import serial
# ser = serial.Serial(port = 'com19',baudrate=4800)  # open serial port
# data = ser.readline()
# # print(data)
# while True: 
#     print(ser.readline())
# print(".............",data.decode())

# data = b'$GPGGA,114959.000,2835.1021,N,07704.3342,E,1,9,0.91,219.0,M,-36.2,M,,0000*70\r\n'
data = b'$GPRMC,115009.000,A,2835.1022,N,07704.3345,E,0.03,0.00,260624,,,A*6D\r\n'
# data =b'$GPGLL,5109.0262317,N,11401.8407304,W,202725.00,A,D*79'

decoded_data = data.decode()
# # print(type(decoded_data))
new_data = decoded_data.split(',')
print(new_data)
if '$GPGGA' in new_data:
    print("GPGGA")
    time = new_data[1]
    latitude = new_data[2]
    latitude_dir = new_data[3]
    longitude = new_data[4]
    longitude_dir = new_data[5]
    print("time", time)
    print("latitude",round(float(latitude),4))
    print("latitude_dir",latitude_dir)
    print("longitude",round(float(longitude),4))
    print("longitude_dir",longitude_dir)
    print("****************************")

# data = b'$GPRMC,115009.000,A,2835.1022,N,07704.3345,E,0.03,0.00,260624,,,A*6D\r\n'
elif '$GPRMC' in new_data:
    print("GPRMC")
    time = new_data[1]
    print(type(time))
    latitude = new_data[3]
    latitude_dir = new_data[4]
    longitude = new_data[5]
    longitude_dir = new_data[6]
    date = new_data[9]
    print("time: ", time)
    print("latitude: ",round(float(latitude),4))
    print("latitude_dir: ",latitude_dir)
    print("longitude: ",round(float(longitude),4))
    print("longitude_dir: ",longitude_dir)
    print("date: ",date)
    print(type(date))
    print("****************************")
# data =b'$GPGLL,5109.0262317,N,11401.8407304,W,202725.00,A,D*79'
elif '$GPGLL' in new_data:
    print("$GPGLL")
    latitude = new_data[1]
    latitude_dir = new_data[2]
    longitude = new_data[3]
    longitude_dir = new_data[4]
    time = new_data[5]
    print("time", time)
    print("latitude",round(float(latitude),4))
    print("latitude_dir",latitude_dir)
    print("longitude",round(float(longitude),4))
    print("longitude_dir",longitude_dir)
    print("****************************")





# **********************for fetching data only when we records is available****************
# records = False
# while True:
#     print("before reading GPS data")
#     data = ser.readline()
#     print("After reading GPS DATA")
#     if records ==True:
#         print(data)
#     else :
#         print("Now it's printing data")
#         records=True
