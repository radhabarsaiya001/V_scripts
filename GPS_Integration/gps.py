import port_fetching
import serial
import reverse_geocoder as rg
import time
class GPS:
    def __init__(self):
        self.ser = None

    def setup_serial(self):
        port = port_fetching.port()
        try:
            self.ser = serial.Serial(port=port, baudrate=4800)
        except serial.SerialException:
            self.ser = None

    def process(self):
        self.setup_serial()
        if not self.ser:
            # print("Not able to communicate, please check the GPS connectivity.")
            return "Not able to communicate, please check the GPS connectivity."

        while True:
            try:
                if self.ser:
                    data =self.ser.readline().decode()
                    new_data = data.split(',')
                    if new_data[2] =="" or new_data[3] =="":
                        print("Loading.............")
                    elif '$GPGGA' in new_data:
                        latitude = round(float(new_data[2]),4)
                        latitude_dir = new_data[3]
                        longitude = round(float(new_data[4]),4)
                        longitude_dir = new_data[5]
                        lat, long = self.dir_sign(latitude, latitude_dir, longitude, longitude_dir)
                        lat = self.lat_dmin_ddgr(lat)
                        long = self.long_dmin_ddgr(long)
                        address = rg.search((lat,long))
                        yield lat, long,address               
                    else:
                        pass
            except UnboundLocalError:
                return "Not able to communicate, please Check the GPS connectivity."

            except UnicodeDecodeError:
                pass

            except Exception as e:
                return f"{e}"


    def dir_sign(self, latitude, latitude_dir, longitude, longitude_dir):
        if latitude_dir == 'S':
            latitude = -latitude
        if longitude_dir == 'W':
            longitude = -longitude
        return latitude, longitude
    
    def lat_dmin_ddgr(self, lat):
        degrees = int(lat / 100)
        minutes = lat - (degrees * 100)
        lat_decimal = degrees + (minutes / 60)
        return round(lat_decimal, 6)
        
    def long_dmin_ddgr(self, long):
        degrees = int(long / 100)
        minutes = long - (degrees * 100)
        long_decimal = degrees + (minutes / 60)
        return round(long_decimal, 6)
        
    # def start(self):
    #     result = self.process()
    #     while True:
    #         for lat, long, addr in result:
    #             if isinstance(lat, str):  # Check if an error message is returned
    #                 return lat  # Return the error message
    #             yield lat, long, addr

    def start(self):
        while True:
            result = self.process()
            if result:
                for lat, long,addr in result:
                    yield lat, long, addr
                    time.sleep(900)   # 15 min. delay

    # def start(self):
    #     for result in self.process():
    #         if isinstance(result, str):
    #             print(result)
    #             break
    #         yield result


# if __name__ == "__main__":
#     gps = GPS()
    # result = gps.start()
    # for data in result:
    #     if isinstance(data, str):
    #         print(data)
    #         break
    #     lat, long, addr = data
    #     print(f"{lat},{long},>>>>>>>>>>>>>>>>>{addr[0]['name']}, {addr[0]['admin2']}, {addr[0]['admin1']}, {addr[0]['cc']}") 
    
    
if __name__ == "__main__":
    gps = GPS()
    for lat,long,addr in gps.start():
        print(f"{lat},{long},>>>>>>>>>>>>>>>>>{addr[0]['name']}, {addr[0]['admin2']}, {addr[0]['admin1']}, { addr[0]['cc']}")


