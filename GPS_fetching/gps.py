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
        except:
            pass
        while True:
            # data =ser.readline().decode()
            # new_data = data.split(',')
            try:
                if ser:
                    data =ser.readline().decode()
                    # print(data)
                    new_data = data.split(',')
                    # print(new_data)
                    if new_data[2] =="" or new_data[3] =="":
                        print("Loading.............")
                    elif '$GPGGA' in new_data:
                        # print(data)
                        time = new_data[1].split('.')
                        time = time[0]
                        loghader= new_data[0]
                        latitude = round(float(new_data[2]),4)
                        latitude_dir = new_data[3]
                        longitude = round(float(new_data[4]),4)
                        longitude_dir = new_data[5]
                        lat = str(latitude) + latitude_dir
                        long = str(longitude) +longitude_dir
                        try:
                            ist_time = fmt.date_formating(time)
                        except Exception as e:
                            print("Time formatting issue in GPGGA Log hadder.")
                            # print(e)

                        # print(loghader)
                        # print("time", time)
                        # print("latitude",latitude)
                        # print("latitude_dir",latitude_dir)
                        # print("longitude",longitude)
                        # print("longitude_dir",longitude_dir)
                        # print("****************************")
                        print(f"{loghader}, {lat}, {long}, {ist_time}")
                        # return loghader,lat, long, time
                        # yield loghader,lat, long, time
                    elif '$GPRMC' in new_data:
                        # print(data)
                        loghader= new_data[0]
                        time = new_data[1].split('.')
                        time = time[0]
                        # print(type(time))
                        latitude = round(float(new_data[3]),4)
                        latitude_dir = new_data[4]
                        longitude = round(float(new_data[5]),4)
                        longitude_dir = new_data[6]
                        date = new_data[9]
                        lat = str(latitude) + latitude_dir
                        long = str(longitude) +longitude_dir
                        date_time = time+date
                        ist_datetime = fmt.date_formating(date_time=date_time)
                        # print(loghader)
                        # print("time: ", time)
                        # print("latitude: ",latitude)
                        # print("latitude_dir: ",latitude_dir)
                        # print("longitude: ",longitude)
                        # print("longitude_dir: ",longitude_dir)
                        # print("date: ",date)
                        # print("IST_DATETIME",ist_datetime)
                        # print(type(date))
                        print("****************************")
                        print(f"{loghader}, {lat}, {long}, {ist_datetime}")
                        # return loghader, lat, long, time, date
                        # yield loghader,lat, long, date_time
                    
                    else:
                        pass
                        # print("Invalid Data, Lat long not acceptable.")
                        # return None
            except UnboundLocalError:
                # print("Not able to communicate, please Check the GPS connectivity.")
                return "Not able to communicate, please Check the GPS connectivity."

            except UnicodeDecodeError:
                pass

            # except :


            except Exception as e:
                # return f"{e}"
                print(e)
            
# obj = GPS.GPS()
# obj

# port = port_fetching.port()
# ser = serial.Serial(baudrate=4800,port= port)
# # while True:
# data = ser.readline()
# print(data) 


# a = b'$GPGGA,120516.000,2835.1199,N,07704.3437,E,1,6,1.34,215.0,M,-36.2,M,,0000*7A\r\n'
# b=a.decode()
# print(b)



