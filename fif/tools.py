import os
from datetime import datetime
import sys
from math import ceil, sqrt

def change_ext(filename, ext):
    """
    change filename extension
    """
    return os.path.splitext(filename)[0] + "." + ext


def get_unique_filename(filename):
    curr_time = datetime.now()
    formatted_time = curr_time.strftime('%Y%m%d%H%M%S%f')
    return os.path.splitext(filename)[0] + "_" + formatted_time + os.path.splitext(filename)[1]
    
def is_file_empty(filename):
    if os.path.getsize(filename) == 0:
        print("Error! file is empty --> ", filename)
        sys.exit()

def calc_size(INPUT_BYTES_LENGHT, mode):
    """
    calculates nearest square image size for byte length
    
    returns tuple: (output_size, extra_bytes_lenght)
    """
    if str(mode) == "1":
        print("1 coming soon")
        sys.exit()
    if mode == "L":
        w = ceil(sqrt(INPUT_BYTES_LENGHT))
        output_size = (w, w)
        OUTPUT_BYTES_LENGHT = w * w
        extra_bytes_lenght = OUTPUT_BYTES_LENGHT - INPUT_BYTES_LENGHT
        return (output_size, extra_bytes_lenght)
    if mode == "RGB":
        w = ceil(sqrt(INPUT_BYTES_LENGHT/3))
        output_size = (w, w)
        OUTPUT_BYTES_LENGHT = w * w * 3
        extra_bytes_lenght = OUTPUT_BYTES_LENGHT - INPUT_BYTES_LENGHT
        return (output_size, extra_bytes_lenght)
    if mode == "RGBA":
        print("rgba coming soon")
        sys.exit()




