# This file contains helper functions tp assist combineImages() in pasting a drop in image
# onto an input image.

import argparse
import uuid
import os
import mimetypes
from PIL import Image, ImageEnhance
from random import randint
from enum import Enum, unique

# If use parser to set input images.
parser = argparse.ArgumentParser(description='Process input and drop in images.')
parser.add_argument('--image', dest='inputFileName', default='ImageInput.png',
                    help='images to be processed (default: ImageInput.png)')

parser.add_argument('--dropin', dest='dropinFileName', default='dropin.png',
                    help='images to be processed (default: ImageInput.png)')

args = parser.parse_args()
#print(args)
#print(dir(args))
print(args.inputFileName)
print(args.dropinFileName)

# Blur index enum
class BlurrIndex(Enum):
    blur = 0.0
    origin = 1.0
    sharpen = 2.0

# Add addon_name to the end of input_name
def file_name_addon(input_name, addon_name):
    input_file = os.path.splitext(input_name)
    result_name = input_file[0] + addon_name + input_file[1]
    return result_name

# Return a new file name which is a result of tow file names combined.
def file_names_combine(name_one, name_two):
    file_one = os.path.splitext(name_one)
    file_two = os.path.splitext(name_two)
    result_file = file_one[0] + "_" + file_two[0] + file_one[1]
    return result_file

# Return a blurred image
def blur_image(image, index) -> object:
    blurrer = ImageEnhance.Sharpness(image)
    return blurrer.enhance(index)

# Blur drop_in_image, sharpen drop_in_image then
# Paste drop_in_image onto the bottom of input_image
def combineImages(input_image, drop_in_image):
    output_name = file_names_combine(input_image, drop_in_image)
    with Image.open(input_image) as image:
        # Sharpen drop in image
        dropin = Image.open(drop_in_image, 'r')
        dropin = ImageEnhance.Color(dropin).enhance(1.20)
        dropin = blur_image(blur_image(blur_image(dropin, BlurrIndex.sharpen.value),
                                       BlurrIndex.sharpen.value),
                            BlurrIndex.sharpen.value)
        # Blur input image
        image = ImageEnhance.Color(image).enhance(0.70)
        image = blur_image(blur_image(blur_image(image, BlurrIndex.blur.value),
                                      BlurrIndex.blur.value),
                           BlurrIndex.blur.value)

        # Debug codes
        print("sharpen value: ", BlurrIndex.sharpen.value)
        print("blur value: ", BlurrIndex.blur.value)

        # Calculate position for drop in image
        # Place the drop in picture randomly horizontally at the bottom of input image.
        x = randint(0, image.width - dropin.width)
        y = image.height - dropin.height

        # Combine images
        image.paste(dropin, box=(x, y), mask=dropin)
        image.save(output_name)

# Proceed
input_image = args.inputFileName
dropin_image = args.dropinFileName

combineImages(input_image, dropin_image)
