from flask import Flask, jsonify, request
import plotting as plt
app = Flask(__name__)
@app.route('/',methods=["POST"])
def fun():
    data = request.get_json()
    plt.plot(img_path=data['img'],
             record_id=data['record_id'],
             speed=data['speed'],
             speed_zone=data['speed_zone'],
             distance=data['distance'],
             direction=data['direction'],
             veh_type = data['veh_type'],
             veh_no= data['veh_no'],
             veh_ctg= data['veh_ctg'],
             voilation= data['violation'],
             operator_name= data['operator_name'],
             op_id=data['op_id'],
             lat = data['lat'],
             long = data['long'],
             col_b = data['col_b'],
             col_g = data['col_g'],
             col_r = data['col_r'],
             loc=data['loc'])

    return jsonify("Success")

if __name__ =="__main__":
    app.run(debug=True)