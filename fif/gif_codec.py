from PIL import Image
import filetype
import os
from datetime import datetime


def encode(filename, gifsize=(200,200), verbose=False):
    output_filename = os.path.splitext(filename)[0] + ".gif"
    if os.path.getsize(filename) == 0:
        print("Error! file is empty --> ", filename)
        sys.exit()
    try:    
        with open(filename, 'rb') as f:
            data = f.read()
    except IOError as e:
        print(e)
        sys.exit()
    WIDTH = gifsize[0]
    HEIGHT = gifsize[1]
    CHUNK_SIZE = int((WIDTH * HEIGHT))
    input_bytes_lenght = len(data)
    chunks = []
    offset = 0
    frames = []
    extra_bytes_lenght = 0
    while offset < input_bytes_lenght:
        chunks.append(data[offset:offset+CHUNK_SIZE])
        offset += CHUNK_SIZE
    for frame_num, chunk in enumerate(chunks):
        padded_chunk = chunk + (b'\0' * (CHUNK_SIZE - len(chunk)))
        # print(frame_num + 1, (WIDTH, HEIGHT), len(padded_chunk))
        extra_bytes_lenght = (CHUNK_SIZE - len(chunk))
        im = Image.frombytes('L', (WIDTH, HEIGHT), padded_chunk)
        im = im.convert(mode="L")
        frames.append(im)
    if verbose:
        print(input_bytes_lenght, "Input file bytes")
        print(extra_bytes_lenght, "Extra bytes added (to fill the last frame)")
        print("Gif size:", str(WIDTH) + "x" + str(HEIGHT))
    
    
    if os.path.isfile(output_filename):
        if verbose:
            print(f"File exist!: {output_filename}")
        curr_time = datetime.now()
        formatted_time = curr_time.strftime('%Y%m%d%H%M%S%f')
        output_filename = os.path.splitext(filename)[0] + "_" + formatted_time + ".gif"
        if verbose:
            print(f"Renamed without overwrite: {output_filename}")
    # write gif - comment kısmına ekstra bayt miktarı eklenecek
    frames[0].save(output_filename, comment=filename, save_all=True, append_images=frames[1:], duration=100, loop=0)
    if verbose:
        print("Saved file -->:", output_filename)

def decode(filename, verbose=False):
    output_filename = ""
    gif = Image.open(filename)
    filename_from_comment = str(gif.info.get("comment"),"utf-8")
    filename_ext_from_comment = os.path.splitext(filename_from_comment)[1]
    # print(filename_ext_from_comment)
    hidden_data = bytearray()  # New empty byte array
    for frame in range(0, gif.n_frames):
        gif.seek(frame)
        hidden_data.extend(gif.tobytes()) # Append gif frames to the hidden_data
    # kind = filetype.guess(hidden_data)
    # if kind is None:
    #     print(f'Cannot guess embedded file type in {filename}!')
    #     return
    # # is output filename exist?
    # if os.path.isfile(os.path.splitext(filename)[0] + "." + filename_ext_from_comment):
    if os.path.isfile(filename_from_comment):
        curr_time = datetime.now()
        formatted_time = curr_time.strftime('%Y%m%d%H%M%S%f')
        # output_filename = os.path.splitext(filename)[0] + "_" + formatted_time + "." + filename_ext_from_comment
        output_filename = os.path.splitext(filename_from_comment)[0] + "_" + formatted_time + filename_ext_from_comment
        if verbose:
            print(f"File exist!: '{filename}' renamed to '{output_filename}'")
    else:
        output_filename = filename_from_comment
    try:    
        with open(output_filename,"wb") as file:
            file.write(hidden_data)
    except IOError as e:
        print(e)
        sys.exit()
    if verbose:

        print(f"'{filename_from_comment}' extracted from '{filename}'")
        # print(f"MIME: {kind.mime}")
        print(f"Saved file ----> {output_filename}")
