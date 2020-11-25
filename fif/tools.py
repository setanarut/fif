import os
from datetime import datetime


def change_ext(filename, ext):
    return os.path.splitext(filename)[0] + "." + ext


def get_unique_filename(filename):
    curr_time = datetime.now()
    formatted_time = curr_time.strftime('%Y%m%d%H%M%S%f')
    return os.path.splitext(filename)[0] + "_" + formatted_time + os.path.splitext(filename)[1]