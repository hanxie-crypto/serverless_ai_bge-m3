import os

current_working_directory = os.getcwd()
parent_directory = os.path.dirname(os.path.dirname(current_working_directory))
bge_m3_dir = os.environ.get('MODEL_M3_PATH',f'{parent_directory}/models/bge-m3')
