#!/usr/bin/python3

"""
PDF Merger

Usage:
    merge <image-folder> <file-name>

Arguments:
    <image-folder>      The folder containing the images you want to merge as a PDF.
    <file-name>         The name you want for your PDF file.

Options:
    -h --help           Show this screen.
"""
import os

from PIL import Image
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    output_name = arguments['<file-name>']
    source_folder = os.path.abspath(arguments['<image-folder>'])
    supported_ext = ['.png', '.jpg', '.jpeg']

    if not os.path.isdir(source_folder):
        raise Exception(f'The given image-folder is not a directory ({source_folder})')

    files = [f for f in os.listdir(source_folder) if os.path.isfile(f'{source_folder}/{f}')]
    pages = []

    for f in sorted(files):
        _, file_ext = os.path.splitext(f)
        if file_ext not in supported_ext:
            print(f'The file "{f}" cannot be converted to pdf and is ignored')

        image = Image.open(f'{source_folder}/{f}')
        im = image.convert('RGB')
        pages.append(im)

    pages[0].save(output_name, save_all=True, append_images=pages[1:])
