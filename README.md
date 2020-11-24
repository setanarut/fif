# FIF (File in File)

FIF is a command line tool for embedding any file into image, audio and video files and decoding back.
Under development! please see CHANGELOG.md

## installation

`pip3 install git+https://github.com/hazarek/fif.git`

## usage

Song.mp3 file as grayscale GIF animation

```shell
fif --encode gif Song.mp3
# saved file -> Song.gif
```

Extract Song.mp3 from GIF container

```shell
fif Song.gif
# saved file -> Song.mp3
```

```shell
usage: fif [-h] [-e {png,wav,gif}] [-v] input

positional arguments:
  input                 input file path

optional arguments:
  -h, --help            show this help message and exit
  -e {png,wav,gif}, --encode {png,wav,gif}
                        encode file
  -v, --verbose         increase output verbosity
  ```
