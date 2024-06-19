from onvif import ONVIFCamera

path = r"C:\Users\hp\miniconda3\Lib\site-packages\onvif_zeep-0.2.12-py3.11.egg\Lib\site-packages\wsdl"
mycam = ONVIFCamera('192.168.1.63', 80, 'admin', 'vinayan@123',path)

# # Get the Network interface service
net_service = mycam.create_devicemgmt_service()

# # Get the network interfaces
interfaces = net_service.GetNetworkInterfaces()
print(interfaces)
interface_token = interfaces[0].token
# print(interface_token)


# # # New IP configuration
new_ip_address = '192.168.1.63'
new_netmask = '255.255.255.0'
new_gateway = '192.168.1.1'

# Set the new IP address
# response = net_service.SetIPAddress(
#     {
#         'InterfaceToken': interface_token,
#         'NetworkInterface': {
#             'IPv4': {
#                 'Enabled': True,
#                 'Manual': {
#                     'Address': new_ip_address,
#                     'PrefixLength': 24
#                 },
#                 'DHCP': False
#             },
#             'IPv6': {
#                 'Enabled': False
#             }
#         }
#     }
# )

# if response:
#     print(f"IP address of the camera has been changed to {new_ip_address}")

# # # # Update the network interface configuration
# # net_service.SetNetworkInterfaces({
# #     'InterfaceToken': interface_token,
# #     'NetworkInterface': {
# #         'IPv4': ip_settings,
# #         'IPv6': {
# #             'Enabled': False
# #         }
# #     }
# # })

# # # # Set the default gateway
# # # net_service.SetNetworkDefaultGateway({
# # #     'IPv4Address': new_gateway
# # # })

# # # print(f"IP address of the camera has been changed to {new_ip_address}")

