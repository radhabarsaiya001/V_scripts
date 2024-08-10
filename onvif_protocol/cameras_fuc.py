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

    def day_night(self, mode):
        media_service = self.mycam.create_media_service()
        imaging_service = self.mycam.create_imaging_service()
        video_sources = media_service.GetVideoSources()
        video_source_token = video_sources[0].token
        current_settings = imaging_service.GetImagingSettings({'VideoSourceToken': video_source_token})
        # print(current_settings)
        desired_mode = mode               #'OFF', 'ON', 'AUTO'
        current_settings.IrCutFilter = desired_mode
        imaging_service.SetImagingSettings({'VideoSourceToken': video_source_token, 'ImagingSettings': current_settings, 'ForcePersistence': True})
        # updated_settings = imaging_service.GetImagingSettings({'VideoSourceToken': video_source_token})
        # if hasattr(updated_settings, 'IrCutFilter'):
        #     print(f"Updated IR Cut Filter Mode: {updated_settings.IrCutFilter}")

    def color_mode(self,mode):
        image=self.mycam.create_imaging_service()
        media_service = self.mycam.create_media_service()
        imagingrequest=image.create_type('SetImagingSettings')
        video_sources=media_service.GetVideoSources()
        imagingrequest.VideoSourceToken=video_sources[0].token
        if mode =="color":
            imagingrequest.ImagingSettings={'Sharpness':150, 'ColorSaturation': 200, 'Contrast':180, 'Brightness':128}
            image.SetImagingSettings(imagingrequest)
        elif mode =="BW":
            imagingrequest.ImagingSettings={'Sharpness':180, 'ColorSaturation': 0, 'Contrast':220, 'Brightness':144}
            image.SetImagingSettings(imagingrequest)
        else:
            return "Not valid mode"
        
    def focus(self):
        image=self.mycam.create_imaging_service()
        media_service = self.mycam.create_media_service()
        imagingrequest=image.create_type('SetImagingSettings')
        video_sources=media_service.GetVideoSources()
        imagingrequest.VideoSourceToken=video_sources[0].token
        imagingrequest.ImagingSettings={'Focus': {'AutoFocusMode' : 'AUTO'}}
        image.SetImagingSettings(imagingrequest)

    def network_setting(self,new_ip_address,new_netmask, new_gateway):
        devicemgmt = self.mycam.create_devicemgmt_service()
        network_interfaces = devicemgmt.GetNetworkInterfaces()
        # print(network_interfaces)
        interface_token = network_interfaces[0].token

        # Create a network interface configuration
        interface_config = devicemgmt.create_type('SetNetworkInterfaces')
        interface_config.InterfaceToken = interface_token
        interface_config.NetworkInterface = {
            'IPv4': {
                'Enabled': True,
                'Manual': [{'Address': new_ip_address, 'PrefixLength': new_netmask}],
                'DHCP': False
            }
        }
        response = devicemgmt.SetNetworkInterfaces(interface_config)
        # print(f"SetNetworkInterfaces response: {response}")
        # print("Successfully Ip updated")


    def video_setting(self,desired_fps, desired_resolution_width, desired_resolution_height, desired_bitrate, desired_quality, desired_gov_length):
        media_service = self.mycam.create_media_service()
        profiles = media_service.GetProfiles()
        video_encoder_configuration = media_service.GetVideoEncoderConfiguration({'ConfigurationToken': profiles[0].VideoEncoderConfiguration.token})
        video_encoder_configuration.RateControl.FrameRateLimit = desired_fps
        video_encoder_configuration.Resolution.Width = desired_resolution_width
        video_encoder_configuration.Resolution.Height = desired_resolution_height
        video_encoder_configuration.RateControl.BitrateLimit = desired_bitrate
        video_encoder_configuration.Quality = desired_quality
        if video_encoder_configuration.Encoding in ['H264', 'H265']:
            video_encoder_configuration.H264.GovLength = desired_gov_length  # or video_encoder_configuration.H265.GovLength for H265

        # Update the video encoder configuration
        media_service.SetVideoEncoderConfiguration({'Configuration': video_encoder_configuration, 'ForcePersistence': True})
        # video_encoder_configuration = media_service.GetVideoEncoderConfiguration({'ConfigurationToken': profiles[0].VideoEncoderConfiguration.token})
        # print(f"Current FPS: {video_encoder_configuration.RateControl.FrameRateLimit}")
        # print(f"Current Resolution: {video_encoder_configuration.Resolution.Width}x{video_encoder_configuration.Resolution.Height}")
        # print(f"Current Bitrate: {video_encoder_configuration.RateControl.BitrateLimit} kbps")
        # print(f"Current Quality: {video_encoder_configuration.Quality}")
        # print(f"Current GOV Length: {video_encoder_configuration.H264.GovLength if video_encoder_configuration.Encoding == 'H264' else 'N/A'}")



# obj= camera_extraction()
# obj.color_mode('color')
# obj.focus()
# obj.color_mode('BW')
# obj.day_night()
# obj.focus()
# obj.ptz( -0.6,0.5,0.2)

# new_ip_address = '192.168.1.67'
# new_netmask = 24
# new_gateway = '192.168.1.1'
# obj.network_setting(new_ip_address,new_netmask, new_gateway)



# obj.day_night('ON')

# desired_fps = 17
# desired_resolution_width = 1920
# desired_resolution_height = 1080
# desired_bitrate = 2048  # in kbps
# desired_quality = 7  # Typically a value between 1 (low) and 10 (high)
# desired_gov_length = 50  #between 10 to 100 streaming length after encoding

# obj.video_setting(desired_fps, desired_resolution_width, desired_resolution_height, desired_bitrate, desired_quality, desired_gov_length)