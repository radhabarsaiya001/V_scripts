import os

# Define the relative path to the XML file
relative_path = 'OpenCV-Face-Recognition/FaceDetection/Cascades/haarcascade_frontalface_default.xml'

# Define the base directory where the XML file is located
base_directory = r'C:\Users\hp\Downloads\Vinayan_New\Face Recognition System'

# Combine the base directory with the relative path to get the full absolute path
absolute_xml_path = os.path.join(base_directory, relative_path)

# Check if the file exists at the absolute path
if os.path.exists(absolute_xml_path):
    print("Path is correct. The XML file exists.")
    print(f"Full path: {absolute_xml_path}")
else:
    print("Path is incorrect. The XML file does not exist.")
