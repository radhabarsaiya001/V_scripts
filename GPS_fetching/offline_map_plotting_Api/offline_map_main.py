import reverse_geocoder as rg
import time
import folium

def reverseGeocode(coordinates):
    result = rg.search(coordinates)
    return result

def onmap(point,loc):
    map = folium.Map(location=point, zoom_start=15)
    folium.Marker(point, popup=loc).add_to(map)
    map.save("final_map_done.html")
    return "success"


# if __name__=="__main__":
#     lat =  28.584885
#     long =  77.0723316
#     coordinates =(lat, long)
#     start = time.time()
#     res = reverseGeocode(coordinates)
#     address = res[0]['admin2']
#     point =[lat,long]
#     onmap(point,address)
#     end = time.time()
#     time_cal = end -start
#     print(time_cal)
