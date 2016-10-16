# 12_image_resize

usage: image_resize.py [-h] [--width WIDTH] [--height HEIGHT] [--scale SCALE]
                       [--output OUTPUT]
                       sourcefile

positional arguments:
  sourcefile       source file for conversion

optional arguments:
  -h, --help       show this help message and exit
  --width WIDTH    set width of output picture
  --height HEIGHT  set height of output picture
  --scale SCALE    set resize scale of output picture
  --output OUTPUT  output file path

 Main purpose of the script - to resize source image file to necessary size
 If "--scale" parameter provided - all other size parameters are ignored
 Script cannot generate picture with higher resolution than provided(checkings are provided)!