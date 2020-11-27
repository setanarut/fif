import os
from datetime import datetime
import sys

def change_ext(filename, ext):
    return os.path.splitext(filename)[0] + "." + ext


def get_unique_filename(filename):
    curr_time = datetime.now()
    formatted_time = curr_time.strftime('%Y%m%d%H%M%S%f')
    return os.path.splitext(filename)[0] + "_" + formatted_time + os.path.splitext(filename)[1]
    
def is_file_empty(filename):
    if os.path.getsize(filename) == 0:
        print("Error! file is empty --> ", filename)
        sys.exit()