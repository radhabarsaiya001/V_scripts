import psutil
import win32api
import shutil
import os

def list_usb_drives_with_names():
    drives = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if 'removable' in partition.opts:
            drive_info = {}
            drive_info['device'] = partition.device
            try:
                drive_info['name'] = win32api.GetVolumeInformation(partition.device)[0]
            except:
                drive_info['name'] = "Unknown"
            drives.append(drive_info)
    return drives

def copy_folder_to_usb(source_folder, destination_drive):
    try:
        destination_folder = os.path.join(destination_drive,os.path.basename(source_folder))
        shutil.copytree(source_folder,destination_folder)
        print(f"Folder copied successfully to {destination_folder}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    usb_drives = list_usb_drives_with_names()
    if usb_drives:
        print("Connected USB Drives:")
        for idx,drive in enumerate(usb_drives):
            # print(drive)
            print(f"{idx}, Drive: {drive['device']}, Name: {drive['name']}")

        selected_drive_idx = int(input("select the USB drive index:"))
        selected_drive = usb_drives[selected_drive_idx]['device']

        source_folder = input("Enter sourc path:")
        if os.path.isdir(source_folder):
            copy_folder_to_usb(source_folder,selected_drive)
        else :
            print("Invalid folder path")
    else:
        print("No USB drives connected.")
