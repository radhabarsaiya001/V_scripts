from onvif import ONVIFCamera
path = r"C:\Users\hp\miniconda3\Lib\site-packages\onvif_zeep-0.2.12-py3.11.egg\Lib\site-packages\wsdl"
mycam = ONVIFCamera('192.168.1.64',80, 'admin','vinayan@123',path)
# device_management = mycam.create_devicemgmt_service()
# network_interfaces = device_management.GetNetworkInterfaces()
# for interface in network_interfaces:
#     print(f"Network Interface: {interface.token}, Enabled: {interface.Enabled}")

# # Get the network protocols
# network_protocols = device_management.GetNetworkProtocols()
# for protocol in network_protocols:
#     print(f"Protocol: {protocol.Name}, Port: {protocol.Port}, Enabled: {protocol.Enabled}")

# # Update HTTP and RTSP ports
# # http_port = 82  # Desired HTTP port
# # rtsp_port = 554  # Desired RTSP port

# # # # Create a function to update a specific protocol port
# # def update_protocol_port(protocols, protocol_name, new_port):
# #     for protocol in protocols:
# #         if protocol.Name == protocol_name:
# #             print(f"Updating {protocol_name} port from {protocol.Port} to {new_port}")
# #             protocol.Port = new_port
# #             protocol.Enabled = True  # Ensure the protocol is enabled
# #             return protocol
# #     return None














# # # media_service = mycam.create_media_service()
# # # profiles = media_service.GetProfiles()
# # # print(profiles)
# # # profile_token = profiles[0].token
# # # video_encoder_configuration = media_service.GetVideoEncoderConfiguration({'ConfigurationToken': profiles[0].VideoEncoderConfiguration.token})

# # def video_setting(desired_fps, desired_resolution_width, desired_resolution_height, desired_bitrate, desired_quality, desired_gov_length):
# #     media_service = mycam.create_media_service()
# #     profiles = media_service.GetProfiles()
# #     video_encoder_configuration = media_service.GetVideoEncoderConfiguration({'ConfigurationToken': profiles[0].VideoEncoderConfiguration.token})
# #     video_encoder_configuration.RateControl.FrameRateLimit = desired_fps
# #     video_encoder_configuration.Resolution.Width = desired_resolution_width
# #     video_encoder_configuration.Resolution.Height = desired_resolution_height
# #     video_encoder_configuration.RateControl.BitrateLimit = desired_bitrate
# #     video_encoder_configuration.Quality = desired_quality
# #     if video_encoder_configuration.Encoding in ['H264', 'H265']:
# #         video_encoder_configuration.H264.GovLength = desired_gov_length  # or video_encoder_configuration.H265.GovLength for H265

# #     # Update the video encoder configuration
# #     media_service.SetVideoEncoderConfiguration({'Configuration': video_encoder_configuration, 'ForcePersistence': True})
# #     # video_encoder_configuration = media_service.GetVideoEncoderConfiguration({'ConfigurationToken': profiles[0].VideoEncoderConfiguration.token})
# #     # print(f"Current FPS: {video_encoder_configuration.RateControl.FrameRateLimit}")
# #     # print(f"Current Resolution: {video_encoder_configuration.Resolution.Width}x{video_encoder_configuration.Resolution.Height}")
# #     # print(f"Current Bitrate: {video_encoder_configuration.RateControl.BitrateLimit} kbps")
# #     # print(f"Current Quality: {video_encoder_configuration.Quality}")
# #     # print(f"Current GOV Length: {video_encoder_configuration.H264.GovLength if video_encoder_configuration.Encoding == 'H264' else 'N/A'}")





# # desired_fps = 10
# # desired_resolution_width = 1920
# # desired_resolution_height = 1080
# # desired_bitrate = 2048  # in kbps
# # desired_quality = 7  # Typically a value between 1 (low) and 10 (high)
# # desired_gov_length = 50  #between 10 to 100 streaming length after encoding


# # video_setting(desired_fps, desired_resolution_width, desired_resolution_height, desired_bitrate, desired_quality, desired_gov_length)






# Create the media service
media_service = mycam.create_media_service()

# Get the available video sources
video_sources = media_service.GetVideoSources()

# Select the first video source (you can adjust this if needed)
video_source_token = video_sources[0].token

# # Get the list of all profiles
profiles = media_service.GetProfiles()

# # Iterate through each profile to get video encoding settings
# for profile in profiles:
#     print(f"Profile: {profile.Name}")
#     if profile.VideoEncoderConfiguration:
#         encoding = profile.VideoEncoderConfiguration.Encoding
#         print(f"  Video Encoding: {encoding}")
#         print(f"  Resolution: {profile.VideoEncoderConfiguration.Resolution.Width}x{profile.VideoEncoderConfiguration.Resolution.Height}")
#         print(f"  Frame Rate: {profile.VideoEncoderConfiguration.RateControl.FrameRateLimit}")
#         print(f"  Bitrate: {profile.VideoEncoderConfiguration.RateControl.BitrateLimit}")
#     else:
#         print("  No Video Encoder Configuration available for this profile.")

# configurations = media_service.GetVideoEncoderConfigurations()
# # print(configurations)
# # Iterate through the configurations and list the encoding options
# for config in configurations:
#     print(f"Configuration Token: {config.token}")
#     print(f"Name: {config.Name}")
#     print(f"Encoding: {config.Encoding}")
#     print(f"Resolution: {config.Resolution.Width}x{config.Resolution.Height}")
#     print(f"Frame Rate Limit: {config.RateControl.FrameRateLimit}")
#     print(f"Bitrate Limit: {config.RateControl.BitrateLimit}")
#     print(f"Quality: {config.Quality}")
#     print("------")



profile_token = profiles[0].token
options = media_service.GetVideoEncoderConfigurationOptions({'ProfileToken': profile_token})
print(options)
# for encoding in options.Encoding:
#     print(f"  - {encoding}")
print("Available Encoding Options:")
print("JPEG Support:", options.JPEG )
print("MPEG4 Support:", options.MPEG4 )
print("H264 Support:", options.H264 )
print("H265 Support:", options.H265 )
