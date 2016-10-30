import argparse
from PIL import Image
import os


def save_new_image(filename, image, width, height, out_filename):
    source_filename, source_extension = os.path.splitext(filename)

    image.thumbnail((width, height))
    if out_filename is not None:
        outfile = out_filename
    else:
        outfile = "{}___{}x{}{}".format(source_filename, width, height, source_extension)
    image.save(outfile, "JPEG")


def open_image(source_path):
    return Image.open(source_path)


def get_new_size(scale, width, height, source_size):
    source_width, source_height = source_size
    source_proportion = source_width / source_height
    if scale is not None:
        width, height = int(scale * source_width), int(scale * source_height)
    elif width is not None and height is None:
        height = int(width / source_proportion)
    elif height is not None and width is None:
        width = int(height * source_proportion)
    elif height is None and width is None:
        width = source_width
        height = source_height
    return width, height


def limit_size(new_value, old_value):
    if new_value >= old_value:
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

    image = open_image(args.sourcefile)
    source_filename, source_extension = os.path.splitext(args.sourcefile)
    source_width, source_height = image.size
    width, height = get_new_size(args.scale, args.width, args.height, image.size)
    if width > source_width or height > source_height:
        print("We cannot create higher resolution!")
    if int(source_width / source_height) != int(width / height):
        print("Proportion of the image changed!")
    width = limit_size(width, source_width)
    height = limit_size(height, source_height)
    save_new_image(args.sourcefile, image, width, height, args.output)
