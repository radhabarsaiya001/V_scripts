from onvif import ONVIFCamera
path = r"C:\Users\hp\miniconda3\Lib\site-packages\onvif_zeep-0.2.12-py3.11.egg\Lib\site-packages\wsdl"
mycam = ONVIFCamera('192.168.1.69', 80, 'admin', 'vinayan@123',path)
new_ip_address = '192.168.1.64'
new_netmask = 24
new_gateway = '192.168.1.1'
def network_setting(new_ip_address,new_netmask, new_gateway):
    devicemgmt = mycam.create_devicemgmt_service()
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
    print("Successfully Ip updated")

network_setting(new_ip_address,new_netmask, new_gateway)

