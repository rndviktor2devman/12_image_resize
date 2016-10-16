import argparse
from PIL import Image
import os


def resize_image(args):
    im = Image.open(args.sourcefile)
    source_filename, source_extension = os.path.splitext(args.sourcefile)
    source_width, source_height = im.size

    width, height = get_new_size(args, source_width, source_height)
    im.thumbnail((width, height))
    if args.output is not None:
        outfile = args.output
    else:
        outfile = "{}___{}x{}{}".format(source_filename, width, height, source_extension)
    im.save(outfile, "JPEG")


def get_new_size(args, source_width, source_height):
    source_proportion = source_width / source_height
    if args.scale is not None:
        scale = check_wrong_size(args.scale, 1)
        width, height = int(scale * source_width), int(scale * source_height)
    elif args.width is not None and args.height is None:
        width = check_wrong_size(args.width, source_width)
        height = int(width / source_proportion)
    elif args.height is not None and args.width is None:
        height = check_wrong_size(args.height, source_height)
        width = int(height * source_proportion)
    elif args.height is not None and args.width is not None:
        if args.width / args.height != source_proportion:
            print("Proportion of the image is changed!")
        width = check_wrong_size(args.width, source_width)
        height = check_wrong_size(args.height, source_height)
    else:
        print("Size of the picture wasn't changed!")
        width = source_width
        height = source_height
    return width, height


def check_wrong_size(new_value, old_value):
    if new_value >= old_value:
        print("We cannot create higher resolution!")
        return old_value
    return new_value


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("sourcefile", type=str, help="source file for conversion")
    parser.add_argument("--width", type=int, help="set width of output picture")
    parser.add_argument("--height", type=int, help="set height of output picture")
    parser.add_argument("--scale", type=float, help="set resize scale of output picture")
    parser.add_argument("--output", type=str, help="output file path")
    args = parser.parse_args()
    resize_image(args)
