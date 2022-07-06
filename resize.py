#!/usr/bin/env python3

import os
from glob import glob
from PIL import Image
from PIL import ImageEnhance
import argparse

name = "librairie.jpg"
size=[416,416]
image = Image.open(name)
image = image.resize(size)
image.save(name)