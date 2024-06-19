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

if __name__ =="__main__":
    app.run(debug=True,host='localhost',port=5000)





# from onvif import ONVIFCamera
# path = r"C:\Users\hp\miniconda3\Lib\site-packages\onvif_zeep-0.2.12-py3.11.egg\Lib\site-packages\wsdl"
# mycam = ONVIFCamera('192.168.1.64', 80, 'admin', 'vinayan@123',path)
# media = mycam.create_media_service()
# ptz = mycam.create_ptz_service()
# media_profile = media.GetProfiles()[0]

# moverequest = ptz.create_type('AbsoluteMove')
# moverequest.ProfileToken = media_profile.token
# moverequest.Position=ptz.GetStatus({'ProfileToken': media_profile.token}).Position

# try: 
#     pan =0.1
#     tilt=0
#     zoom=0
#     moverequest.Position.PanTilt.x = float(pan)
#     moverequest.Position.PanTilt.y = float(tilt)
#     moverequest.Position.Zoom.x = float(zoom)
# except:
#     pass
    
# ptz.AbsoluteMove(moverequest)