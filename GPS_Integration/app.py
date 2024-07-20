from flask import Flask, request, jsonify
# from process_GPS_data import GPS
from gps import GPS
app = Flask(__name__)
@app.route('/')
def get_data():
    try:
        # gps = GPS()
        # for lat,long,addr in gps.start():
        #     print(f"{lat},{long},>>>>>>>>>>>>>>>>>{addr[0]['name']}, {addr[0]['admin2']}, {addr[0]['admin1']}, { addr[0]['cc']}")
        gps = GPS()
        result = []
        for lat, long, addr in gps.start():
            result.append({
                "latitude": lat,
                "longitude": long,
                "address": {
                    "name": addr[0]['name'],
                    "admin2": addr[0]['admin2'],
                    "admin1": addr[0]['admin1'],
                    "cc": addr[0]['cc']
                }
            })
        return jsonify(result)    
    except Exception as e:
        return jsonify({"Error": str(e), "status": 500})
if __name__ =="__main__":
    app.run(debug=True)
