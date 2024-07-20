# # from gps import GPS
# # while True:
# #     data = GPS.GPS()
# #     lat = data[1]
# #     long = data[2]



# # import time



# # def func1():
# #     while True:
# #         a = 5
# #         b= 10
# #         yield a,b
# #         a+=1
# #         b+=2
# #         time.sleep(0.5)

# # while True:
# #     data = func1()


# # a = b'$GPGGA,120516.000,2835.1199,N,07704.3437,E,1,6,1.34,215.0,M,-36.2,M,,0000*7A\r\n'

# def fun():
#     a = b'$GPGGA,120516.000,2835.1199,N,07704.3437,E,1,6,1.34,215.0,M,-36.2,M,,0000*7A\r\n'
#     b=a.decode()
#     new_data = b.split(',')
#     latitude = round(float(new_data[2]),4)
#     latitude_dir = new_data[3]
#     longitude = round(float(new_data[4]),4)
#     longitude_dir = new_data[5]

#     lat, long = prc(latitude, latitude_dir, longitude, longitude_dir)
#     lat = lat_dmin_ddgr(lat)
#     long = long_dmin_ddgr(long)
#     return lat, long

# def prc(latitude,latitude_dir, longitude,longitude_dir):
#     if latitude_dir =='S' and longitude_dir =="W":
#         latitude = -latitude
#         longitude = -longitude
#     elif latitude_dir =='N' and longitude_dir =="W":
#         longitude = -longitude
#     elif latitude_dir =='S' and longitude_dir =="E":
#         latitude = -latitude
#     else:
#         pass
#     return  latitude,longitude

# def lat_dmin_ddgr(lat):
#     lat = lat/100
#     lat_splited = str(lat).split('.')
#     lat_minutes = int(lat_splited[1])/10000
#     lat_decimal = lat_minutes/60
#     lat_degree = int(lat_splited[0])
#     lat = round(lat_degree+lat_decimal, 6)
#     return lat

# def long_dmin_ddgr(long):
#     try:
#         long = long/100
#         long_splited = str(long).split('.')
#         long_minutes = int(long_splited[1])/10000
#         long_decimal = long_minutes/60
#         long_degree = int(long_splited[0])
#         long = round(long_degree+long_decimal, 6)
#         return long
#     except:
#         return "longitude decimal minute to decimal degree conversion issue......"



# obj = fun()
# print(obj)



# # def fun():
# #     print("Hii Radha")
# #     def fun_in():
# #         a= 5
# #         fun_iner_mst = fun_i2()
# #         return a, fun_iner_mst, "Hii it's main"
# #     def fun_i2():
# #         return "Hii inner most process fun\n"
# #     obj = fun_in()
# #     return obj

# # obj = fun()
# # print(obj)


# import time
# class GPS:
#     def __init__(self):
#         pass
#     def GPS(self):
#         while True:
#             def process(self):
#                 try:
#                     a = b'$GPGGA,120516.000,2835.1199,N,07704.3437,E,1,6,1.34,215.0,M,-36.2,M,,0000*7A\r\n'
#                     b=a.decode()
#                     new_data = b.split(',')
#                     latitude = round(float(new_data[2]),4)
#                     latitude_dir = new_data[3]
#                     longitude = round(float(new_data[4]),4)
#                     longitude_dir = new_data[5]
#                     lat, long = dir_sign(latitude, latitude_dir, longitude, longitude_dir)
#                     lat = lat_dmin_ddgr(lat)
#                     long = long_dmin_ddgr(long)
#                     yield lat, long
                
#                 except UnboundLocalError:
#                     # print("Not able to communicate, please Check the GPS connectivity.")
#                     return "Not able to communicate, please Check the GPS connectivity."

#                 except UnicodeDecodeError:
#                     pass

#                 except Exception as e:
#                     return f"{e}"


#             def dir_sign(self,latitude,latitude_dir, longitude,longitude_dir):
#                 try:
#                     if latitude_dir =='S' and longitude_dir =="W":
#                         latitude = -latitude
#                         longitude = -longitude
#                     elif latitude_dir =='N' and longitude_dir =="W":
#                         longitude = -longitude
#                     elif latitude_dir =='S' and longitude_dir =="E":
#                         latitude = -latitude
#                     else:
#                         pass
#                     return  latitude,longitude   
#                 except:
#                     return "GPS direction coneversion issue......"

#             def lat_dmin_ddgr(self,lat):
#                 try:
#                     lat = lat/100
#                     lat_splited = str(lat).split('.')
#                     lat_minutes = int(lat_splited[1])/10000
#                     lat_decimal = lat_minutes/60
#                     lat_degree = int(lat_splited[0])
#                     lat = round(lat_degree+lat_decimal, 6)
#                     return lat
#                 except:
#                     return "latitude decimal minute to decimal degree conversion issue......"
                
#             def long_dmin_ddgr(self,long):
#                 try:
#                     long = long/100
#                     long_splited = str(long).split('.')
#                     long_minutes = int(long_splited[1])/10000
#                     long_decimal = long_minutes/60
#                     long_degree = int(long_splited[0])
#                     long = round(long_degree+long_decimal, 6)
#                     return long
#                 except:
#                     return "longitude decimal minute to decimal degree conversion issue......"
            
#             def start(self):
#                 while True:
#                     result = self.process()
#                     if result:
#                         for lat, long in result:
#                             print(f"Latitude: {lat}, Longitude: {long}")

# if __name__ == "__main__":
#     gps = GPS()
#     gps.start()




import time
import reverse_geocoder as rg
class GPS:
    def __init__(self):
        pass

    def process(self):
            while True:
                try:
                    a = b'$GPGGA,120516.000,2835.1199,N,07704.3437,E,1,6,1.34,215.0,M,-36.2,M,,0000*7A\r\n'
                    b=a.decode()
                    new_data = b.split(',')
                    if '$GPGGA' in new_data:
                        latitude = round(float(new_data[2]), 4)
                        latitude_dir = new_data[3]
                        longitude = round(float(new_data[4]), 4)
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
        try:
            if latitude_dir == 'S' and longitude_dir == "W":
                latitude = -latitude
                longitude = -longitude
            elif latitude_dir == 'N' and longitude_dir == "W":
                longitude = -longitude
            elif latitude_dir == 'S' and longitude_dir == "E":
                latitude = -latitude
            return latitude, longitude
        except:
            return "GPS direction conversion issue......"

    def lat_dmin_ddgr(self, lat):
        try:
            lat = lat / 100
            lat_splited = str(lat).split('.')
            lat_minutes = int(lat_splited[1]) / 10000
            lat_decimal = lat_minutes / 60
            lat_degree = int(lat_splited[0])
            lat = round(lat_degree + lat_decimal, 6)
            return lat
        except:
            return "latitude decimal minute to decimal degree conversion issue......"

    def long_dmin_ddgr(self, long):
        try:
            long = long / 100
            long_splited = str(long).split('.')
            long_minutes = int(long_splited[1]) / 10000
            long_decimal = long_minutes / 60
            long_degree = int(long_splited[0])
            long = round(long_degree + long_decimal, 6)
            return long
        except:
            return "longitude decimal minute to decimal degree conversion issue......"

    # def start(self):
    #     while True:
    #         result = self.process()
    #         if result:
    #             for lat, long,addr in result:
    #                 yield lat, long, addr
    #                 # print(f"Latitude: {lat}, Longitude: {long}")

    def start(self):
        while True:
            result = self.process()
            if result:
                for lat, long,addr in result:
                    yield lat, long, addr
                    # print(f"Latitude: {lat}, Longitude: {long}")


# if __name__ == "__main__":
#     gps = GPS()
#     # gps.start()
#     for lat,long,addr in gps.start():
#         # print(f"{lat},{long},>>>>>>>>>>>>>>>>>{nearset_town}, {district}, {state}, {country}")
#         print(f"{lat},{long},>>>>.........>>>>>>>>>>>>>{addr[0]['name']}, {addr[0]['admin2']}, {addr[0]['admin1']}, { addr[0]['cc']}")

