import sys
import argparse
import os
import time
import filetype
from fif import gif_codec, wav_codec, png_codec
from fif.tools import *

# sys.tracebacklimit = 0


def getargs():
    parser = argparse.ArgumentParser(description="FIF is a command line tool for embedding any file into GIF, PNG and WAV files and decoding back.")
    parser.add_argument(
        "-e",
        "--encode",
        help="encode file",
        type=str,
        choices=(
            "png",
            "wav",
            "gif"))
    parser.add_argument(
        "-m",
        "--mode",
        help="Image mode",
        type=str,
        choices=(
            "1",
            "L",
            "P",
            "RGB",
            "RGBA"))
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase output verbosity")
    parser.add_argument("input", type=str, help="Input file path")
    return parser.parse_args()


def run_fif():
    args = getargs()
    is_file_empty(args.input)
    if args.encode is None:
        kind = filetype.guess(args.input)
        if kind.mime == "image/gif":
            if args.verbose:
                print('Container MIME type: %s' % kind.mime)
            gif_codec.decode(args.input, verbose=args.verbose)
        elif kind.mime == "image/png":
            png_codec.decode(args.input, verbose=args.verbose)
        elif kind.mime == "audio/x-wav":
            wav_codec.decode(args.input, verbose=args.verbose)
        else:
            print("Unsupported container MIME type!")
    if args.encode == "gif":
        if args.mode != None:
            gif_codec.encode(args.input, mode=args.mode, verbose=args.verbose)
        else:
            gif_codec.encode(args.input, verbose=args.verbose)
                
    elif args.encode == "png":
        if args.mode != None:
            png_codec.encode(args.input, mode=args.mode, verbose=args.verbose)
        else:
            png_codec.encode(args.input, verbose=args.verbose)
            
    elif args.encode == "wav":
        wav_codec.encode(args.input, verbose=args.verbose)
