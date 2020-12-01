import sys
import argparse
import os
import time
import filetype
from fif import gif_codec, wav_codec, png_codec
from fif.tools import *

# sys.tracebacklimit = 0


def getargs():
    parser = argparse.ArgumentParser()
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
                print('Container file extension: %s' % kind.extension)
                print('Container MIME type: %s' % kind.mime)
            gif_codec.decode(args.input, verbose=args.verbose)
        elif kind.mime == "image/png":
            png_codec.decode(args.input, verbose=args.verbose)
        elif kind.mime == "audio/x-wav":
            wav_codec.decode(args.input, verbose=args.verbose)
        else:
            print("Unsupported MIME")
    if args.encode == "gif":
        gif_codec.encode(args.input, verbose=args.verbose)
    elif args.encode == "png":
        png_codec.encode(args.input, verbose=args.verbose)
    elif args.encode == "wav":
        wav_codec.encode(args.input, verbose=args.verbose)

        # wav_codec.encode(args.input, verbose=args.verbose)
