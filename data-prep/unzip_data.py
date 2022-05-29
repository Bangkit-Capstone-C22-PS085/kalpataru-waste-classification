# Import and mount Google drive to given access
import os
import zipfile
from google.colab import drive
drive.mount('/content/drive')

# Path to access data
base_path = "/content/drive/Shareddrives/capstone-project-c22-ps085/ML/dataset/trashnet_data"
os.listdir(base_path)

# Process unzipping data
try:
    dir = 'data'
    path = os.path.join(base_path, dir)
    os.mkdir(path)
    print("Directory created")
except FileExistsError:
    print("Directory existed")

data_zip = 'dataset-resized.zip'
dir = os.path.join(base_path, 'data')
with zipfile.ZipFile(os.path.join(base_path, data_zip), 'r') as zip_ref:
    zip_ref.extractall(dir)