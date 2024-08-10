# from onvif import ONVIFCamera
# path = r"C:\Users\hp\miniconda3\Lib\site-packages\onvif_zeep-0.2.12-py3.11.egg\Lib\site-packages\wsdl"
# mycam = ONVIFCamera('192.168.1.64',80, 'admin','vinayan@123',path)
# media_service = mycam.create_media_service()
# video_sources = media_service.GetVideoSources()
# # print(video_sources)
# video_source_token = video_sources[0].token
# imaging_service = mycam.create_imaging_service()
# current_settings = imaging_service.GetImagingSettings({'VideoSourceToken': video_source_token})
# # if hasattr(current_settings, 'IrCutFilter'):
# #     print(f"Current IR Cut Filter Mode: {current_settings.IrCutFilter}")

# desired_mode = 'OFF'
# current_settings.IrCutFilter = desired_mode
# imaging_service.SetImagingSettings({'VideoSourceToken': video_source_token, 'ImagingSettings': current_settings, 'ForcePersistence': True})
# # updated_settings = imaging_service.GetImagingSettings({'VideoSourceToken': video_source_token})
# # if hasattr(updated_settings, 'IrCutFilter'):
# #     print(f"Updated IR Cut Filter Mode: {updated_settings.IrCutFilter}")




