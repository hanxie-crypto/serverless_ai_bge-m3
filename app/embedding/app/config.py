import os

current_working_directory = os.getcwd()
bge_m3_dir = os.environ.get('MODEL_M3_PATH',f'{current_working_directory}/app/models/bge-m3')
