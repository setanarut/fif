# # Encode inputfile as a series of RGB video frames
# # Frames are written to frames/frameNNNN.png

# import png
# import os

# input_filename = "youtube-dl-master.zip"

# with open(input_filename, 'rb') as f:
#     data = f.read()

# WIDTH, HEIGHT = 854, 480

# CHUNK_SIZE = int(WIDTH * HEIGHT ) * 3

# chunks = []
# offset = 0


# while offset < len(data):
#     chunks.append(data[offset:offset+CHUNK_SIZE])
#     offset += CHUNK_SIZE

# print(len(data), len(chunks[-1]),len(chunks),CHUNK_SIZE)
# print()

# # last_chunk = chunks[-1] + (b'\0' * (CHUNK_SIZE - len(chunks[-1])))
# # print(len(padded_chunk))

# for frame_num, chunk in enumerate(chunks):
    
#     #chunk boyutundan küçükse byte ekler.eşitse eklemez(b'\0' * 0)
#     padded_chunk = chunk + (b'\0' * (CHUNK_SIZE - len(chunk)))
    
#     # print(frame_num + 1, (WIDTH, HEIGHT), len(padded_chunk))
    
#     f = open('frames/frame%04d.png' % (frame_num + 1), 'wb')
#     w = png.Writer(size=(WIDTH, HEIGHT), greyscale=False, alpha=False)
#     w.write_array(f, padded_chunk)
#     f.close()

# # encode
# os.system("ffmpeg -i frames/frame%04d.png -vcodec ffv1 out.mkv")

# # decode
# os.system("ffmpeg -i out.mkv -pix_fmt rgb24 -f rawvideo " + "decoded_" + input_filename)

# # Encode as video with:
# # ffmpeg -i frames/frame%04d.png -vf scale=1440:1080 -sws_flags neighbor -vcodec ffv1 output.mkv
# # Decode the resulting downloaded video with:
# # ffmpeg -i output.mkv -vf scale=120:-1,eq=contrast=10 -sws_flags neighbor -pix_fmt monob -f rawvideo o.pdf

