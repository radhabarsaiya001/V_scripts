# import port_fetching
# import serial
# import reverse_geocoder as rg

# class GPS:
#     def __init__(self):
#         self.ser = None

#     def setup_serial(self):
#         port = port_fetching.port()
#         try:
#             self.ser = serial.Serial(port=port, baudrate=4800)
#         except serial.SerialException:
#             self.ser = None

#     def process(self):
#         self.setup_serial()
#         if not self.ser:
#             return "Not able to communicate, please check the GPS connectivity."

#         while True:
#             try:
#                 data = self.ser.readline().decode()
#                 new_data = data.split(',')
#                 if new_data[2] == "" or new_data[3] == "":
#                     print("Loading.............")
#                 elif '$GPGGA' in new_data:
#                     latitude, latitude_dir = float(new_data[2]), new_data[3]
#                     longitude, longitude_dir = float(new_data[4]), new_data[5]

#                     lat, long = self.dir_sign(latitude, latitude_dir, longitude, longitude_dir)
#                     lat = self.lat_dmin_ddgr(lat)
#                     long = self.long_dmin_ddgr(long)

#                     address = rg.search((lat, long))
#                     yield lat, long, address
#             except UnicodeDecodeError:
#                 pass
#             except Exception as e:
#                 return str(e)

#     def dir_sign(self, latitude, latitude_dir, longitude, longitude_dir):
#         if latitude_dir == 'S':
#             latitude = -latitude
#         if longitude_dir == 'W':
#             longitude = -longitude
#         return latitude, longitude

#     def lat_dmin_ddgr(self, lat):
#         lat = lat / 100
#         lat_deg = int(lat)
#         lat_min = (lat - lat_deg) * 100
#         lat_decimal = lat_min / 60
#         return round(lat_deg + lat_decimal, 6)

#     def long_dmin_ddgr(self, long):
#         long = long / 100
#         long_deg = int(long)
#         long_min = (long - long_deg) * 100
#         long_decimal = long_min / 60
#         return round(long_deg + long_decimal, 6)

#     def start(self):
#         for result in self.process():
#             if isinstance(result, str):
#                 print(result)
#                 break
#             yield result

# if __name__ == "__main__":
#     gps = GPS()
#     for lat, long, addr in gps.start():
#         print(f"{lat},{long}, {addr[0]['name']}, {addr[0]['admin2']}, {addr[0]['admin1']}, {addr[0]['cc']}")





def ddmm_mmmm_to_decimal_degrees(ddmm_mmmm):
    # Convert the input to a float
    ddmm_mmmm = float(ddmm_mmmm)
    
    # Extract the degrees
    degrees = int(ddmm_mmmm / 100)
    
    # Extract the minutes
    minutes = ddmm_mmmm - (degrees * 100)
    
    # Convert to decimal degrees
    decimal_degrees = degrees + (minutes / 60)
    
    return decimal_degrees

# Example usage
ddmm_mmmm = 2834.9745
result = ddmm_mmmm_to_decimal_degrees(ddmm_mmmm)
print(f"{ddmm_mmmm} in DDMM.MMMM format is equal to {result} decimal degrees")
