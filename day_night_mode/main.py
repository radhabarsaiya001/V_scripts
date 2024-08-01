import requests

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

payload = """<?xml version="1.0" encoding="UTF-8"?>
<IrLight>
    <brightnessLevel>60</brightnessLevel>
    <nightBrightnessLevel>20</nightBrightnessLevel>
    <grayToColorDelay>10</grayToColorDelay>
    <colorToGrayDelay>10</colorToGrayDelay>
    <type>color</type>
    <mode>gray</mode>
    <sunRiseTime>06:00:00</sunRiseTime>
    <sunSetTime>18:00:00</sunSetTime>
    <infraredLampMode>2</infraredLampMode>
    <infraredLampPower>50</infraredLampPower>
    <sensitivityLevel>1</sensitivityLevel>
    <FarinfraredLampPower>50</FarinfraredLampPower>
    <midInfraRedLampPower>100</midInfraRedLampPower>
    <laserBrightness>100</laserBrightness>
    <laserAngle>50</laserAngle>
    <laserLampPower>100</laserLampPower>
</IrLight>"""

response = requests.put(url, headers=headers, data=payload)

if response.status_code == 200:
    print("Day/Night mode changed successfully.")
else:
    print(f"Failed to change Day/Night mode. Status code: {response.status_code}")
