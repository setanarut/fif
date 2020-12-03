from PIL import Image
import os
import sys
from fif.tools import *


def encode(filename, mode="L", gifsize=(200, 200), verbose=False):
    if mode not in ["1", "L", "P"]:
        print("invalid mode choice for GIF: (choose from '1', 'L', 'P')")
        sys.exit()
    if mode in ["1", "P"]:
        print("1, P modes coming soon")
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
        frames.append(Image.frombytes(mode, (width, height), padded_chunk))
    if os.path.isfile(output_filename):
        output_filename = get_unique_filename(output_filename)
    metadata = str(os.path.basename(filename)) + \
        ":" + str(extra_bytes_lenght)
    # write
    frames[0].save(output_filename, comment=metadata, save_all=True,
                   append_images=frames[1:], duration=100, loop=0)
    if verbose:
        print(f"Mode: {mode}")
        print(f"Extra bytes:  {extra_bytes_lenght}")
        print(f"Metadata:  {metadata}")
        print(f"GIF size: {gifsize}")
        print(f"Filename:  {output_filename}")
    sys.exit()


def decode(filename, verbose=False):
    gif = Image.open(filename)
    dir_name = os.path.dirname(filename)
    metadata = str(gif.info.get("comment"), "utf-8").split(":")
    output_filename = os.path.join(dir_name, metadata[0])
    extra_bytes_lenght = int(metadata[1])
    hidden_data = bytearray()  # New empty byte array
    for frame in range(0, gif.n_frames):
        gif.seek(frame)
        # Append gif frames to the hidden_data
        hidden_data.extend(gif.tobytes())
    hidden_data = hidden_data[:-extra_bytes_lenght]  # remove extra bytes
    data_len = len(hidden_data)
    if os.path.isfile(output_filename):
        output_filename = get_unique_filename(output_filename)
    try:
        with open(output_filename, "wb") as file:
            file.write(hidden_data)
    except IOError as e:
        print(e)
        sys.exit()
    if verbose:
        print(f"Bytes: {data_len}")
        print(f"Extra bytes:  {extra_bytes_lenght}")
        print(f"Metadata:  {metadata}")
        print(f"Filename:  {output_filename}")
    sys.exit()
