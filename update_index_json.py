#!/usr/bin/env python

import os

import subprocess

import glob

import sys

import functools

if(sys.version_info.major > 2):
    read_input = input
    reduce = functools.reduce
else:
    read_input = raw_input
    reduce = reduce

path_to_repo_root = os.path.dirname(os.path.abspath(__file__))

os.chdir(path_to_repo_root)

flutter_command = "flutter-beta"

url_base = "https://raw.githubusercontent.com/thefarmerapps/duckz-cdn/master/images"


path_to_images_folder = "{0}/images".format(path_to_repo_root)

all_repo_file_entities = os.walk(path_to_repo_root)

images_filenames = []

for root, dirs, files in all_repo_file_entities:
    for filepath in files:
        filename_lower = filepath.lower()
        if(filename_lower.endswith(".png") or filename_lower.endswith(".jpeg") or filename_lower.endswith(".jpg")):
            images_filenames.append(filepath)


path_to_index_json_file = "{0}/index.json".format(path_to_repo_root)

json = reduce(lambda a, b: a +
              '"{0}/{1}",'.format(url_base, b), images_filenames, "")

json = "[{0}]".format(json)

f = open(path_to_index_json_file, "w")

f.write(json)

f.close()
