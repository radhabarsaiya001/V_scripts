from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/change_day_night_mode', methods=['POST'])
def change_day_night_mode():
    try:
        # Extract parameters from request
        mode = request.json.get('mode')
        FarinfraredLampPower = request.json.get('FarinfraredLampPower')
        infraredLampPower = request.json.get('infraredLampPower')

        # Validate mode
        if mode not in ['color', 'gray']:
            return jsonify({"error": "Invalid mode. Use 'color' or 'gray'."}), 400

        # Validate power levels
        if not (0 <= FarinfraredLampPower <= 100) or not (0 <= infraredLampPower <= 100):
            return jsonify({"error": "Power levels must be between 0 and 100."}), 400

        url = "http://192.168.1.64/CGI/Image/channels/1/irLight"
        headers = {
            "Accept": "application/xml, text/xml, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-IN,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,en-GB;q=0.6,en-US;q=0.5",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/xml; charset=UTF-8",
            "Cookie": "live_port=3002; V2_Session_72788487=036cXGVAIZGOjokIr9tgQlccgJfUy0ol; 192.168.1.64=1%3D0%7C%7C1%260%261",
            "HttpSession": "036cXGVAIZGOjokIr9tgQlccgJfUy0ol",
            "If-Modified-Since": "0",
            "Origin": "http://192.168.1.64",
            "Referer": "http://192.168.1.64/?t=4823265117",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

        payload = f"""<?xml version="1.0" encoding="UTF-8"?>
        <IrLight>
            <brightnessLevel>60</brightnessLevel>
            <nightBrightnessLevel>20</nightBrightnessLevel>
            <grayToColorDelay>10</grayToColorDelay>
            <colorToGrayDelay>10</colorToGrayDelay>
            <type>color</type>
            <mode>{mode}</mode>
            <sunRiseTime>06:00:00</sunRiseTime>
            <sunSetTime>18:00:00</sunSetTime>
            <infraredLampMode>2</infraredLampMode>
            <infraredLampPower>{infraredLampPower}</infraredLampPower>
            <sensitivityLevel>1</sensitivityLevel>
            <FarinfraredLampPower>{FarinfraredLampPower}</FarinfraredLampPower>
            <midInfraRedLampPower>100</midInfraRedLampPower>
            <laserBrightness>100</laserBrightness>
            <laserAngle>50</laserAngle>
            <laserLampPower>100</laserLampPower>
        </IrLight>"""

        response = requests.put(url, headers=headers, data=payload)

        if response.status_code == 200:
            return jsonify({"message": "Day/Night mode and power levels changed successfully."}), 200
        else:
            return jsonify({"error": f"Failed to change settings. Status code: {response.status_code}"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
