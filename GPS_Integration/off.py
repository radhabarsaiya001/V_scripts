import reverse_geocoder as rg

def reverseGeocode(coordinates):
    result = rg.search(coordinates)
    return result
if __name__=="__main__":
    # lat = 23.414449087367526
    # long = 87.50981727834392
    # lat = 25.46973727942246
    # long = 78.55805386950951
    # lat = 13.911795221184313
    # long = -15.60594810394902
    coordinates =(lat, long)
    res = reverseGeocode(coordinates)
    nearset_town = res[0]['name']
    state = res[0]['admin1']
    district = res[0]['admin2']
    country = res[0]['cc']
    print("Country :", country)
    print("state: ",state)
    print("district: ",district)
    print("nearset_town: ", nearset_town)
    print("**********************")
    print(f"Address:>>>>>>>>>............{nearset_town}, {district}, {state}, {country}")