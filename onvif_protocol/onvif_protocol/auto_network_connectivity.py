import subprocess
import os
import time

network_password = "realmme797"

def list_wifi_networks_windows():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'network'], capture_output=True, text=True)
        output = result.stdout
        # print(output)
        networks = []
        for line in output.split('\n'):
            if "SSID" in line:
                ssid = line.split(":")[1].strip()
                if ssid:  # Exclude empty SSID entries
                    networks.append(ssid)
        return networks
    except Exception as e:
        print(f"Error: {e}")
        return []

def create_wifi_profile(ssid, password, filename="wifi_profile.xml"):
    profile_xml = f"""<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{password}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    with open(filename, "w") as file:
        file.write(profile_xml)

def add_wifi_profile(filename="wifi_profile.xml"):
    try:
        subprocess.run(['netsh', 'wlan', 'add', 'profile', f'filename={filename}'], check=True)
        print("Wi-Fi profile added successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add Wi-Fi profile: {e}")

def connect_to_wifi(ssid):
    try:
        subprocess.run(['netsh', 'wlan', 'connect', f'name={ssid}'], check=True)
        print(f"connecting to {ssid}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to {ssid}: {e}")


if __name__ == "__main__":
    current_wifi_netwroks = list_wifi_networks_windows()
    if current_wifi_netwroks:
        print("Current available networks")
        for index,networks in enumerate(current_wifi_netwroks):
            print(f"{index} :{networks}")
        network_ssid_index = int(input("Select any netwroks:"))
        print(current_wifi_netwroks[network_ssid_index])
    network_ssid = current_wifi_netwroks[network_ssid_index]
    create_wifi_profile(network_ssid, network_password)
    add_wifi_profile()
    connect_to_wifi(network_ssid)

