from onvif import ONVIFCamera

class camera_extraction:
    def __init__(self):
        path = r"C:\Users\hp\miniconda3\Lib\site-packages\onvif_zeep-0.2.12-py3.11.egg\Lib\site-packages\wsdl"
        self.mycam = ONVIFCamera('192.168.1.64',80, 'admin','vinayan@123',path)

    def ptz(self,pan,tilt,zoom):
        media = self.mycam.create_media_service()
        ptz = self.mycam.create_ptz_service()
        media_profile = media.GetProfiles()[0]
        # print(media_profile)

        moverequest = ptz.create_type('AbsoluteMove')
        moverequest.ProfileToken = media_profile.token
        moverequest.Position=ptz.GetStatus({'ProfileToken': media_profile.token}).Position
        # print(moverequest.Position)

        try: 
            moverequest.Position.PanTilt.x = float(pan)
            moverequest.Position.PanTilt.y = float(tilt)
            moverequest.Position.Zoom.x = float(zoom)
        except Exception as e:
            print("The problem is: ",e)
        
        ptz.AbsoluteMove(moverequest)

# obj= camera_extraction()
# obj.ptz(0,0,0.7)


