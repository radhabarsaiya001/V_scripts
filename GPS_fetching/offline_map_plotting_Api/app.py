from flask import Flask, request, jsonify
import offline_map_main as mp
app = Flask(__name__)
@app.route('/',methods=['POST'])
def plot():
    try:
        data = request.get_json()
        lat = data.get('lat')
        long = data.get('long')
        coordinates =(lat, long)
        res = mp.reverseGeocode(coordinates)
        address = res[0]['admin2']
        point =[lat,long]
        mp.onmap(point,address)
        return "successfully img saved.."
    except Exception as e:
        return jsonify({"Error": str(e), "status": 500})
    
if __name__ =="__main__":
    app.run(debug=True)

