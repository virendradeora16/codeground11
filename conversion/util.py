import json
import os 
from conversion.path import Path
def read_mapping_file():
    config = None
    if os.path.exists(Path.config_path.value):
        config = json.load(open(Path.config_path.value))
    return config