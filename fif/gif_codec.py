from PIL import Image
import filetype
import os
import sys
from fif.tools import *


def encode(filename, gifsize=(200, 200), verbose=False):
    if os.path.getsize(filename) == 0:
        print("Error! file is empty --> ", filename)
        sys.exit()
    try:
        with open(filename, 'rb') as f:
            data = f.read()
    except IOError as e:
        print(e)
        sys.exit()

    output_filename = change_ext(filename, "gif")
    width = gifsize[0]
    height = gifsize[1]
    chunk_size = int((width * height))
    INPUT_BYTES_LENGHT = len(data)
    chunks = []
    offset = 0
    frames = []
    extra_bytes_lenght = 0
    while offset < INPUT_BYTES_LENGHT:
        chunks.append(data[offset:offset + chunk_size])
        offset += chunk_size
    for frame_num, chunk in enumerate(chunks):
        padded_chunk = chunk + (b'\0' * (chunk_size - len(chunk)))
        extra_bytes_lenght = (chunk_size - len(chunk))
        frames.append(Image.frombytes('L', (width, height), padded_chunk))

    if os.path.isfile(output_filename):
        output_filename = get_unique_filename(output_filename)
        if verbose:
            print(
                f"file has been renamed to: '{output_filename}'")
    print("file -> ", output_filename)

    required_info = str(os.path.basename(filename)) + \
        ":" + str(extra_bytes_lenght)

    # write
    frames[0].save(output_filename, comment=required_info, save_all=True,
                   append_images=frames[1:], duration=100, loop=0)

    if verbose:
        print(INPUT_BYTES_LENGHT, "Input file bytes")
        print("Gif size:", str(width) + "x" + str(height))
        print(
            "Filename and extra byte length has been embedded in gif comment -> ",
            required_info)
        print("DONE")
    sys.exit()


def decode(filename, verbose=False):
    gif = Image.open(filename)
    dir_name = os.path.dirname(filename)
    required_info = str(gif.info.get("comment"), "utf-8").split(":")
    output_filename = os.path.join(dir_name, required_info[0])
    extra_bytes_lenght = int(required_info[1])
    hidden_data = bytearray()  # New empty byte array
    for frame in range(0, gif.n_frames):
        gif.seek(frame)
        # Append gif frames to the hidden_data
        hidden_data.extend(gif.tobytes())

    hidden_data = hidden_data[:-extra_bytes_lenght]

    if os.path.isfile(output_filename):
        output_filename = get_unique_filename(output_filename)
        if verbose:
            print(
                f"There is a file with this name, the file has been renamed to {output_filename}")
    if verbose:
        print(f"'{output_filename}' extracted from '{filename}'")
        print(f"Saved file ----> {output_filename}")
    try:
        with open(output_filename, "wb") as file:
            file.write(hidden_data)
    except IOError as e:
        print(e)
        sys.exit()
