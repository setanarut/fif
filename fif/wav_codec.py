import os
import sys
import re
from fif.tools import *
# out_file.write(input_bytes.lstrip(wavheader_bytes))

# wavheader uzunluk 44
# son 300



def encode(filename, verbose=False):
    with open(filename, "rb") as f:
        data = f.read()
    output_filename = change_ext(filename, "wav")
    wavheader_bytes = b'RIFF$\xa70\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00D\xac\x00\x00\x88X\x01\x00\x02\x00\x10\x00data\x00\xa70\x00'
    base_filename = ":" + os.path.basename(filename)
    base_filename = base_filename.zfill(300)
    HEADER_LEN = 44
    if os.path.isfile(output_filename):
        output_filename = get_unique_filename(output_filename)
    try:
        with open(output_filename, "wb") as file:
            file.write(wavheader_bytes + data + bytes(base_filename, "utf-8"))
    except IOError as e:
        print(e)
        sys.exit()

def decode(filename, verbose=False):
    dir_name = os.path.dirname(filename)
    with open(filename, "rb") as f:
        data = f.read()
    # output_data = output_data.lstrip(wavheader_bytes))
    output_data = bytearray(data)
    output_filename = output_data[-300:].decode("utf-8").split(":")[-1]
    output_data = output_data[44:]
    output_data = output_data[:-300]
    
    if os.path.isfile(output_filename):
        output_filename = get_unique_filename(output_filename)
    try:
        with open(os.path.join(dir_name,output_filename), "wb") as file:
            file.write(output_data)
    except IOError as e:
        print(e)
        sys.exit()


