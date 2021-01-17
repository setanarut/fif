# FIF (File in File)

FIF is a command line tool for embedding any file into GIF, PNG and WAV files and decoding back.

## Installation

`pip3 install fif`

## Usage

dogmalar.mp3 file as grayscale GIF animation

```shell
fif --encode gif test.mp3
# saved file -> test.gif
```
![test_gif](./test.gif)

Extract dogmalar.mp3 from GIF container

```shell
fif test.gif
# saved file -> dogmalar.mp3
```

```shell
positional arguments:
  input                 Input file path

optional arguments:
  -h, --help            show this help message and exit
  -e {png,wav,gif}, --encode {png,wav,gif}
                        encode file
  -m {1,L,P,RGB,RGBA}, --mode {1,L,P,RGB,RGBA}
                        Image mode
  -v, --verbose         Increase output verbosity
  ```
