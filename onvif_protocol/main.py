from cameras_fuc import camera_extraction
from flask import Flask, render_template, request, jsonify

functionality = camera_extraction()
app = Flask(__name__)

@app.route('/ptz',methods=['POST'])
def update_ptz():
    try:
        data = request.get_json()
        pan = data.get('pan')
        tilt = data.get('tilt')
        zoom = data.get('zoom')
        functionality.ptz(pan,tilt,zoom)
        # return jsonify({'pan':pan, 'tilt': tilt, 'zoom':zoom}) ,200
        return jsonify({'msg':"Success",'status':200})
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    
@app.route('/video_setting',methods=['POST'])
def video_setting():
    try:
        data = request.get_json()
        desired_fps = data.get('desired_fps')
        desired_resolution_width = data.get('desired_resolution_width')
        desired_resolution_height = data.get('desired_resolution_height')
        desired_bitrate = data.get('desired_bitrate')
        desired_quality = data.get('desired_quality')
        desired_gov_length = data.get('desired_gov_length')
        functionality.video_setting(desired_fps, desired_resolution_width, desired_resolution_height, desired_bitrate, desired_quality, desired_gov_length)
        return jsonify({'msg':'success','status':200})
    except Exception as e:
        return jsonify({'Error':str(e), 'status':500})
    
@app.route('/network_setting',methods=['POST'])
def network_setting():
    try:
        data = request.get_json()
        new_ip_address = data.get('new_ip_address')
        new_netmask = data.get('new_netmask')
        new_gateway = data.get('new_gateway')
        functionality.network_setting(new_ip_address,new_netmask, new_gateway)
        return jsonify({'msg':'success','status':200})
    except Exception as e:
        return jsonify({'Error':str(e), 'status':500})
    
@app.route('/focus',methods=['POST'])
def focus():
    try:
        functionality.focus()
        return jsonify({'msg':'success','status':200})
    except Exception as e:
        return jsonify({'Error':str(e), 'status':500})
    
@app.route('/color_mode',methods=['POST'])
def color():
    try:
        data = request.get_json()
        mode = data.get('mode')
        functionality.color_mode(mode)
        return jsonify({'msg':'success','status':200})
    except Exception as e:
        return jsonify({'Error':'Ir mode not suppoeted', 'status':500})

if __name__ =="__main__":
    app.run(debug=True,host='localhost',port=5000)
    
@app.route('/daynight_mode',methods=['POST'])
def day_night():
    try:
        data = request.get_json()
        mode = data.get('mode')
        functionality.day_night(mode)
        return jsonify({'msg':'success','status':200})
    except Exception as e:
        return jsonify({'Error':'Ir mode not suppoeted', 'status':500})

if __name__ =="__main__":
    app.run(debug=True,host='localhost',port=5000)
p

# {
#     "pan": -0.6,
#     "tilt": 0.5,
#     "zoom":0.2
# }


# {
#     "mode":"ON"   //'OFF', 'AUTO'
# }

# {
#   "desired_fps": 17,
#   "desired_resolution_width": 1920,
#   "desired_resolution_height": 1080,
#   "desired_bitrate": 2048,
#   "desired_quality": 7,
#   "desired_gov_length": 50
# }

# {
#   "new_ip_address": "192.168.1.67",
#   "new_netmask": 24,
#   "new_gateway": "192.168.1.1"
# }

# {
#     "mode": "color"    // "BW"
# }

